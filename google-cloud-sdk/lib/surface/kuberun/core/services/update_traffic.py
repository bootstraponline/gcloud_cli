# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""Update traffic settings of a KubeRun service."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.kuberun import flags
from googlecloudsdk.command_lib.kuberun import kuberun_command
from googlecloudsdk.command_lib.kuberun import traffic_pair
from googlecloudsdk.command_lib.kuberun import traffic_printer
from googlecloudsdk.core import exceptions
from googlecloudsdk.core.resource import resource_printer

_DETAILED_HELP = {
    'EXAMPLES':
        """
        To send all traffic to the latest revision, run:

            $ {command} SERVICE --to-latest

        To split the traffic between revisions, run:

            $ {command} SERVICE --to-revisions=rev1=30,rev2=70

        To change the traffic allocated for one revision and let the other
        revisions's traffic auto-resized, run:

            $ {command} SERVICE --to-revisions=rev1=30
        """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class UpdateTraffic(kuberun_command.KubeRunCommand):
  """Updates the traffic settings of a KubeRun service."""

  detailed_help = _DETAILED_HELP
  flags = [
      flags.ClusterConnectionFlags(),
      flags.NamespaceFlag(),
      flags.TrafficFlags(),
      flags.AsyncFlag()
  ]

  @classmethod
  def Args(cls, parser):
    super(UpdateTraffic, cls).Args(parser)
    parser.add_argument(
        'service',
        help='KubeRun service for which to update the traffic settings.')
    resource_printer.RegisterFormatter(
        traffic_printer.TRAFFIC_PRINTER_FORMAT,
        traffic_printer.TrafficPrinter,
        hidden=True)
    parser.display_info.AddFormat(traffic_printer.TRAFFIC_PRINTER_FORMAT)

  def BuildKubeRunArgs(self, args):
    return [args.service] + super(UpdateTraffic, self).BuildKubeRunArgs(args)

  def Command(self):
    return ['core', 'services', 'update-traffic']

  def FormatOutput(self, out, args):
    if out:
      svc = json.loads(out)
      return traffic_pair.GetTrafficTargetPairsDict(
          svc['spec']['traffic'],
          svc.get('status', {}).get('traffic', []),
          svc.get('status', {}).get('latestReadyRevisionName'),
          svc.get('status', {}).get('url'))
    else:
      raise exceptions.Error('Failed to update traffic for service [{}]'.format(
          args.service))
