# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""Utilities for manipulating organization policies."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.resourcesettings import service as settings_service

ORGANIZATION = 'organization'
FOLDER = 'folder'
PROJECT = 'project'


def ComputeResourceType(args):
  """Returns the resource type from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
  """
  if args.organization:
    resource_type = ORGANIZATION
  elif args.folder:
    resource_type = FOLDER
  else:
    resource_type = PROJECT

  return resource_type


def GetCreateRequestFromResourceType(resource_type, parent_resource, setting_id,
                                     setting_value):
  """Returns the get_request from the user-specified arguments.

  Args:
    resource_type: string value object contains resource type
    parent_resource: resource location such as `organizations/123`
    setting_id: setting id such as `iam-projectCreatorRoles`
    setting_value: setting value object contains name, value and (optional) etag
  """

  messages = settings_service.ResourceSettingsMessages()

  if resource_type == ORGANIZATION:
    message_type = messages.ResourcesettingsOrganizationsSettingsValueCreateRequest
  elif resource_type == FOLDER:
    message_type = messages.ResourcesettingsFoldersSettingsValueCreateRequest
  else:
    message_type = messages.ResourcesettingsProjectsSettingsValueCreateRequest

  get_request = message_type(parent=parent_resource,
                             settingsId=setting_id,
                             googleCloudResourcesettingsV1SettingValue
                             =setting_value)

  return get_request


def GetDeleteValueRequestFromArgs(args, setting_name):
  """Returns the get_request from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
    setting_name: setting name such as `settings/iam-projectCreatorRoles`
  """

  messages = settings_service.ResourceSettingsMessages()

  if args.organization:
    get_request = messages.ResourcesettingsOrganizationsSettingsDeleteValueRequest(
        name=setting_name)
  elif args.folder:
    get_request = messages.ResourcesettingsFoldersSettingsDeleteValueRequest(
        name=setting_name)
  else:
    get_request = messages.ResourcesettingsProjectsSettingsDeleteValueRequest(
        name=setting_name)

  return get_request


def GetGetValueRequestFromArgs(args, setting_name):
  """Returns the get_request from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
    setting_name: setting name such as `settings/iam-projectCreatorRoles`
  """

  resource_type = ComputeResourceType(args)

  return GetGetValueRequestFromResourceType(resource_type, setting_name)


def GetGetValueRequestFromResourceType(resource_type, setting_name):
  """Returns the get_request from the user-specified arguments.

  Args:
    resource_type: A String object that contains the resource type
    setting_name: setting name such as `settings/iam-projectCreatorRoles`
  """

  messages = settings_service.ResourceSettingsMessages()

  if resource_type == ORGANIZATION:
    get_request = messages.ResourcesettingsOrganizationsSettingsGetValueRequest(
        name=setting_name)
  elif resource_type == FOLDER:
    get_request = messages.ResourcesettingsFoldersSettingsGetValueRequest(
        name=setting_name)
  else:
    get_request = messages.ResourcesettingsProjectsSettingsGetValueRequest(
        name=setting_name)

  return get_request


def GetLookupEffectiveValueRequestFromArgs(args, parent_resource):
  """Returns the get_request from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
    parent_resource: resource location such as `organizations/123`
  """

  messages = settings_service.ResourceSettingsMessages()

  if args.organization:
    get_request = messages.ResourcesettingsOrganizationsSettingsValueLookupEffectiveValueRequest(
        name=parent_resource)
  elif args.folder:
    get_request = messages.ResourcesettingsFoldersSettingsValueLookupEffectiveValueRequest(
        name=parent_resource)
  else:
    get_request = messages.ResourcesettingsProjectsSettingsValueLookupEffectiveValueRequest(
        name=parent_resource)

  return get_request


def GetListRequestFromArgs(args, parent_resource):
  """Returns the get_request from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
    parent_resource: resource location such as `organizations/123`
  """

  messages = settings_service.ResourceSettingsMessages()

  if args.organization:
    get_request = messages.ResourcesettingsOrganizationsSettingsListRequest(
        parent=parent_resource)
  elif args.folder:
    get_request = messages.ResourcesettingsFoldersSettingsListRequest(
        parent=parent_resource)
  else:
    get_request = messages.ResourcesettingsProjectsSettingsListRequest(
        parent=parent_resource)

  return get_request


def GetSearchRequestFromArgs(args, parent_resource):
  """Returns the get_request from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
    parent_resource: resource location such as `organizations/123`
  """

  messages = settings_service.ResourceSettingsMessages()

  if args.organization:
    get_request = messages.ResourcesettingsOrganizationsSettingsSearchRequest(
        parent=parent_resource)
  elif args.folder:
    get_request = messages.ResourcesettingsFoldersSettingsSearchRequest(
        parent=parent_resource)
  else:
    get_request = messages.ResourcesettingsProjectsSettingsSearchRequest(
        parent=parent_resource)

  return get_request


def GetServiceFromArgs(args):
  """Returns the service from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
  """

  resource_type = ComputeResourceType(args)

  return GetServiceFromResourceType(resource_type)


def GetServiceFromResourceType(resource_type):
  """Returns the service from the resource type input.

  Args:
    resource_type: A String object that contains the resource type
  """

  if resource_type == ORGANIZATION:
    service = settings_service.OrganizationsSettingsService()
  elif resource_type == FOLDER:
    service = settings_service.FoldersSettingsService()
  else:
    service = settings_service.ProjectsSettingsService()

  return service


def GetUpdateValueRequestFromResourceType(resource_type, setting_value):
  """Returns the get_request from the user-specified arguments.

  Args:
    resource_type: A String object that contains the resource type
    setting_value: setting value object contains name, value
  """

  messages = settings_service.ResourceSettingsMessages()

  if resource_type == ORGANIZATION:
    message_type = messages.ResourcesettingsOrganizationsSettingsUpdateValueRequest
  elif resource_type == FOLDER:
    message_type = messages.ResourcesettingsFoldersSettingsUpdateValueRequest
  else:
    message_type = messages.ResourcesettingsProjectsSettingsUpdateValueRequest

  get_request = message_type(name=setting_value.name,
                             googleCloudResourcesettingsV1SettingValue
                             =setting_value)

  return get_request


def GetValueServiceFromArgs(args):
  """Returns the value-service from the user-specified arguments.

  Args:
    args: argparse.Namespace, An object that contains the values for the
      arguments specified in the Args method.
  """

  resource_type = ComputeResourceType(args)

  return GetValueServiceFromResourceType(resource_type)


def GetValueServiceFromResourceType(resource_type):
  """Returns the value-service from the resource type input.

  Args:
    resource_type: A String object that contains the resource type
  """

  if resource_type == ORGANIZATION:
    value_service = settings_service.OrganizationsSettingsValueService()
  elif resource_type == FOLDER:
    value_service = settings_service.FoldersSettingsValueService()
  else:
    value_service = settings_service.ProjectsSettingsValueService()

  return value_service
