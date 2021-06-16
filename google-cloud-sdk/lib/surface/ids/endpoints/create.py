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
"""Create endpoint command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import datetime
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import properties
from googlecloudsdk.api_lib.ids import ids_api
from googlecloudsdk.command_lib.ids import flags

DETAILED_HELP = {
    'DESCRIPTION':
        """
          Create an endpoint for the specified VPC network. Successful creation
          of an endpoint results in an endpoint in READY state. Check the
          progress of endpoint creation by using `gcloud alpha ids endpoints
          list`.

          For more examples, refer to the EXAMPLES section below.


        """,
    'EXAMPLES':
        """
            To create an endpoint called `my-endpoint` for VPC network
            `my-net`, in zone `us-central1-a`, alerting on LOW threats or
            higher, run:

            $ {command} my-endpoint --network=my-net --zone=us-central1-a --project=my-project --severity=LOW

    """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Create(base.CreateCommand):
  """Create a Cloud IDS endpoint."""

  @staticmethod
  def Args(parser):
    flags.AddEndpointResource(parser)
    flags.AddNetworkArg(parser)
    flags.AddDescriptionArg(parser)
    flags.AddSeverityArg(parser)
    base.ASYNC_FLAG.AddToParser(parser)
    labels_util.AddCreateLabelsFlags(parser)

  def Run(self, args):
    endpoint = args.CONCEPTS.endpoint.Parse()
    network = args.network
    severity = args.severity
    description = args.description
    is_async = args.async_

    client = ids_api.Client(self.ReleaseTrack())
    operation = client.CreateEndpoint(endpoint.Name(),
                                      endpoint.Parent().RelativeName(), network,
                                      severity, description)
    # Return the in-progress operation if async is requested.
    if is_async:
      # Delete operations have no format by default,
      # but here we want the operation metadata to be printed.
      if not args.IsSpecified('format'):
        args.format = 'default'
      return operation
    return client.WaitForOperation(
        operation_ref=client.GetOperationRef(operation, endpoint),
        message='waiting for endpoint [{}] to be created'.format(
            endpoint.RelativeName()),
        max_wait=datetime.timedelta(hours=1))


Create.detailed_help = DETAILED_HELP
