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
"""gcloud dns record-sets delete command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dns import util
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dns import flags
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class DeleteBeta(base.DeleteCommand):
  """Delete a record-set in a managed-zone.

  This command deletes a record-set contained within the specified
  managed-zone.

  ## EXAMPLES

  To delete a record-set with dnsName foo.bar.com. and record type A, rrdata
  run:

    $ {command} foo.bar.com. --type=A --zone=my_zone

  """

  @classmethod
  def Args(cls, parser):
    flags.GetZoneArg().AddToParser(parser)
    flags.GetResourceRecordSetsNameArg().AddToParser(parser)
    flags.GetResourceRecordSetsTypeArg(True).AddToParser(parser)
    parser.display_info.AddCacheUpdater(None)

  def Run(self, args):
    api_version = 'v1beta2'
    messages = apis.GetMessagesModule('dns', api_version)

    dns_client = util.GetApiClient(api_version)

    zone_ref = util.GetRegistry(api_version).Parse(
        args.zone,
        params={
            'project': properties.VALUES.core.project.GetOrFail,
        },
        collection='dns.managedZones')

    rrsets_ref = util.GetRegistry(api_version).Parse(
        args.type,
        params={
            'project': properties.VALUES.core.project.GetOrFail,
            'managedZone': args.zone,
            'name': args.name
        },
        collection='dns.resourceRecordSets')

    result = dns_client.resourceRecordSets.Delete(
        messages.DnsResourceRecordSetsDeleteRequest(
            project=zone_ref.project,
            managedZone=zone_ref.Name(),
            name=util.AppendTrailingDot(args.name),
            type=args.type))
    log.DeletedResource(rrsets_ref)

    return result