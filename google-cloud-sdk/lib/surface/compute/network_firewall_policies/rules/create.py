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
"""Command for creating network firewall policy rules."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import firewall_policy_rule_utils as rule_utils
from googlecloudsdk.api_lib.compute.network_firewall_policies import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute.network_firewall_policies import flags


class Create(base.CreateCommand):
  r"""Creates a Compute Engine network firewall policy rule.

  *{command}* is used to create network firewall policy rules.
  """

  NETWORK_FIREWALL_POLICY_ARG = None

  @classmethod
  def Args(cls, parser):
    cls.NETWORK_FIREWALL_POLICY_ARG = flags.NetworkFirewallPolicyRuleArgument(
        required=True, operation='create')
    cls.NETWORK_FIREWALL_POLICY_ARG.AddArgument(parser, operation_type='create')
    flags.AddAction(parser)
    flags.AddFirewallPolicy(parser, operation='inserted')
    flags.AddSrcIpRanges(parser)
    flags.AddDestIpRanges(parser)
    flags.AddLayer4Configs(parser)
    flags.AddDirection(parser)
    flags.AddEnableLogging(parser)
    flags.AddDisabled(parser)
    flags.AddTargetServiceAccounts(parser)
    flags.AddDescription(parser)
    flags.AddSrcSecureTags(parser)
    flags.AddTargetSecureTags(parser)
    parser.display_info.AddCacheUpdater(flags.NetworkFirewallPoliciesCompleter)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    ref = self.NETWORK_FIREWALL_POLICY_ARG.ResolveAsResource(
        args, holder.resources)
    network_firewall_policy_rule_client = client.NetworkFirewallPolicyRule(
        ref=ref,
        compute_client=holder.client)

    src_ip_ranges = []
    dest_ip_ranges = []
    layer4_configs = []
    target_service_accounts = []
    enable_logging = False
    disabled = False
    src_secure_tags = []
    target_secure_tags = []
    if args.IsSpecified('src_ip_ranges'):
      src_ip_ranges = args.src_ip_ranges
    if args.IsSpecified('dest_ip_ranges'):
      dest_ip_ranges = args.dest_ip_ranges
    if args.IsSpecified('layer4_configs'):
      layer4_configs = args.layer4_configs
    if args.IsSpecified('target_service_accounts'):
      target_service_accounts = args.target_service_accounts
    if args.IsSpecified('enable_logging'):
      enable_logging = args.enable_logging
    if args.IsSpecified('disabled'):
      disabled = args.disabled
    if args.IsSpecified('src_secure_tags'):
      src_secure_tags = [
          holder.client.messages.FirewallPolicyRuleSecureTag(name=tag)
          for tag in args.src_secure_tags
      ]
    if args.IsSpecified('target_secure_tags'):
      target_secure_tags = [
          holder.client.messages.FirewallPolicyRuleSecureTag(name=tag)
          for tag in args.target_secure_tags
      ]
    layer4_config_list = rule_utils.ParseLayer4Configs(layer4_configs,
                                                       holder.client.messages)
    matcher = holder.client.messages.FirewallPolicyRuleMatcher(
        srcIpRanges=src_ip_ranges,
        destIpRanges=dest_ip_ranges,
        layer4Configs=layer4_config_list,
        srcSecureTags=src_secure_tags)
    traffic_direct = (holder.client.messages.FirewallPolicyRule
                      .DirectionValueValuesEnum.INGRESS)
    if args.IsSpecified('direction'):
      if args.direction == 'INGRESS':
        traffic_direct = (holder.client.messages.FirewallPolicyRule
                          .DirectionValueValuesEnum.INGRESS)
      else:
        traffic_direct = (holder.client.messages.FirewallPolicyRule
                          .DirectionValueValuesEnum.EGRESS)

    firewall_policy_rule = holder.client.messages.FirewallPolicyRule(
        priority=rule_utils.ConvertPriorityToInt(ref.Name()),
        action=args.action,
        match=matcher,
        direction=traffic_direct,
        targetServiceAccounts=target_service_accounts,
        description=args.description,
        enableLogging=enable_logging,
        disabled=disabled,
        targetSecureTags=target_secure_tags)

    return network_firewall_policy_rule_client.Create(
        firewall_policy=args.firewall_policy,
        firewall_policy_rule=firewall_policy_rule)


Create.detailed_help = {
    'EXAMPLES':
        """\
    To create a rule with priority ``10'' in a network firewall policy with name
    ``my-policy'' and description ``example rule'', run:

        $ {command} 10
            --firewall-policy=my-policy
            --action=allow
            --description="example rule"
    """,
}
