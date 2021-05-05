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
"""Command to list Tensorboard time series in AI platform."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.ai.tensorboard_time_series import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.ai import constants
from googlecloudsdk.command_lib.ai import endpoint_util
from googlecloudsdk.command_lib.ai import flags
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.core import resources


def _GetUri(tensorboard_run):
  ref = resources.REGISTRY.ParseRelativeName(
      tensorboard_run.name,
      constants.TENSORBOARD_TIME_SERIES_COLLECTION,
      api_version=constants.AI_PLATFORM_API_VERSION[constants.ALPHA_VERSION])
  return ref.SelfLink()


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class List(base.ListCommand):
  """List the Tensorboard time series of the given project, region, and Tensorboard run."""

  @staticmethod
  def Args(parser):
    concept_parsers.ConceptParser.ForResource(
        '--tensorboard-run-id',
        flags.GetTensorboardRunResourceSpec(),
        'To list Tensorboard time series',
        required=True).AddToParser(parser)
    parser.display_info.AddUriFunc(_GetUri)

  def _Run(self, args, version):
    tensorboard_run_ref = args.CONCEPTS.tensorboard_run_id.Parse()
    region = tensorboard_run_ref.AsDict()['locationsId']
    with endpoint_util.AiplatformEndpointOverrides(
        version=version, region=region):
      return client.TensorboardTimeSeriesClient(version=version).List(
          tensorboard_run_ref=tensorboard_run_ref,
          limit=args.limit,
          page_size=args.page_size,
          sort_by=args.sort_by)

  def Run(self, args):
    return self._Run(args, constants.ALPHA_VERSION)