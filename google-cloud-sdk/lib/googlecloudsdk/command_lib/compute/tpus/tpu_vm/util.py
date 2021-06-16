# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""CLI Utilities for Cloud TPU VM commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.util import files

import six


def GetProject(release_track, ssh_helper):
  holder = base_classes.ComputeApiHolder(release_track)
  project_name = properties.VALUES.core.project.GetOrFail()
  return ssh_helper.GetProject(holder.client, project_name)


def InvertBoolean(boolean):
  """Inverts the boolean value passed in."""
  return not boolean


def ReadMetadataFromFile(metadata_from_file):
  """Reads the metadata values from the files.

  Args:
    metadata_from_file: dict of metadata keys to filenames.

  Returns:
    A dict of metadata keys to values.
  """
  metadata = {}
  for key, file_path in six.iteritems(metadata_from_file):
    metadata[key] = files.ReadFileContents(file_path)
  return metadata


def GetMessagesModule(version='v2alpha1'):
  return apis.GetMessagesModule('tpu', version)


def StartRequestHook(ref, args, request):
  """Declarative request hook for TPU Start command."""
  del ref
  del args
  start_request = GetMessagesModule().StartNodeRequest()
  request.startNodeRequest = start_request
  return request


def StopRequestHook(ref, args, request):
  """Declarative request hook for TPU Stop command."""
  del ref
  del args
  stop_request = GetMessagesModule().StopNodeRequest()
  request.stopNodeRequest = stop_request
  return request


def IsTPUVMNode(node):
  api_version = six.text_type(node.apiVersion).upper()
  return (not api_version.startswith('V1')
          and api_version != 'API_VERSION_UNSPECIFIED')


def FilterTPUVMNodes(response, args):
  """Removes Cloud TPU V1 API nodes from the 'list' output.

  Used with 'compute tpus tpu-vm list'.

  Args:
    response: response to ListNodes.
    args: the arguments for the list command.

  Returns:
    A response with only TPU VM (non-V1 API) nodes.
  """
  del args
  return list(six.moves.filter(IsTPUVMNode, response))


class GuestAttributesListEntry(object):
  """Holder for GetGuestAttributes output."""

  def __init__(self, worker_id, namespace, key, value):
    self.worker_id = worker_id
    self.namespace = namespace
    self.key = key
    self.value = value


def TransformGuestAttributes(response, args):
  """Transforms the GuestAttributes into a flatter list.

  This is needed to make clearer output in the case of TPU pods, since they have
  many workers.

  Args:
    response: response to GetGuestAttributes.
    args: the arguments for the GetGuestAttributes command.

  Returns:
    A list of GuestAttributesListEntry objects.
  """
  del args
  lst = []
  for i, ga in enumerate(response.guestAttributes):
    for entry in ga.queryValue.items:
      lst.append(
          GuestAttributesListEntry(i, entry.namespace, entry.key, entry.value))
  return lst


def CheckTPUVMNode(response, args):
  """Verifies that the node is a TPU VM node.

  If it is not a TPU VM node, exit with an error instead.

  Args:
    response: response to GetNode.
    args: the arguments for the list command.

  Returns:
    The response to GetNode if the node is TPU VM.
  """
  del args
  if IsTPUVMNode(response):
    return response
  log.err.Print('ERROR: Please use "gcloud compute tpus describe" for Cloud TPU'
                ' nodes that are not TPU VM.')
  sys.exit(1)


class TPUNode(object):
  """Helper to create and modify TPU nodes."""

  def __init__(self):
    self._api_version = 'v2alpha1'
    self.client = apis.GetClientInstance('tpu', self._api_version)
    self.messages = apis.GetMessagesModule('tpu', self._api_version)

  def GetMessages(self):
    return self.messages

  def Get(self, name, zone):
    """Retrieves the TPU node in the given zone."""
    project = properties.VALUES.core.project.Get(required=True)
    fully_qualified_node_name_ref = resources.REGISTRY.Parse(
        name,
        params={
            'locationsId': zone,
            'projectsId': project
        },
        collection='tpu.projects.locations.nodes',
        )
    request = self.messages.TpuProjectsLocationsNodesGetRequest(
        name=fully_qualified_node_name_ref.RelativeName())
    return self.client.projects_locations_nodes.Get(request)

  def GetGuestAttributes(self, name, zone):
    """Retrives the Guest Attributes for the nodes."""
    project = properties.VALUES.core.project.Get(required=True)
    fully_qualified_node_name_ref = resources.REGISTRY.Parse(
        name,
        params={
            'locationsId': zone,
            'projectsId': project
        },
        collection='tpu.projects.locations.nodes',
        )
    request = self.messages.TpuProjectsLocationsNodesGetGuestAttributesRequest(
        name=fully_qualified_node_name_ref.RelativeName())
    return self.client.projects_locations_nodes.GetGuestAttributes(request)

  def UpdateNode(self, name, zone, node, update_mask):
    """Updates the TPU node in the given zone."""
    project = properties.VALUES.core.project.Get(required=True)
    fully_qualified_node_name_ref = resources.REGISTRY.Parse(
        name,
        params={
            'locationsId': zone,
            'projectsId': project
        },
        collection='tpu.projects.locations.nodes',
        )
    request = self.messages.TpuProjectsLocationsNodesPatchRequest(
        name=fully_qualified_node_name_ref.RelativeName(),
        node=node,
        updateMask=update_mask)
    return self.client.projects_locations_nodes.Patch(request)

  def UpdateMetadataKey(self, metadata, key, value):
    """Updates a key in the TPU metadata object.

    If the key does not exist, it is added.

    Args:
      metadata: tpu.messages.Node.MetadataValue, the TPU's metadata.
      key: str, the key to be updated.
      value: str, the new value for the key.

    Returns:
      The updated metadata.
    """
    # If the metadata is empty, return a new metadata object with just the key.
    if metadata is None or metadata.additionalProperties is None:
      return self.messages.Node.MetadataValue(
          additionalProperties=[
              self.messages.Node.MetadataValue.AdditionalProperty(
                  key=key, value=value)])

    item = None
    for x in metadata.additionalProperties:
      if x.key == key:
        item = x
        break
    if item is not None:
      item.value = value
    else:
      # The key is not in the metadata, so append it.
      metadata.additionalProperties.append(
          self.messages.Node.MetadataValue.AdditionalProperty(
              key=key, value=value))
    return metadata
