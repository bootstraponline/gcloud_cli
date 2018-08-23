# -*- coding: utf-8 -*- #
# Copyright 2015 Google Inc. All Rights Reserved.
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
"""Tests for the disks add-iam-policy-binding subcommand."""


from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import textwrap

from apitools.base.py.testing import mock
from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.calliope import base
from tests.lib import cli_test_base
from tests.lib import parameterized
from tests.lib import sdk_test_base
from tests.lib import test_case
from tests.lib.surface.compute import test_resources


@parameterized.parameters(
    (base.ReleaseTrack.ALPHA, 'alpha'),
    (base.ReleaseTrack.BETA, 'beta'))
class AddIamPolicyBindingTest(sdk_test_base.WithFakeAuth,
                              cli_test_base.CliTestBase,
                              parameterized.TestCase):

  def _SetUp(self, track, api_version):
    self.messages = core_apis.GetMessagesModule('compute', api_version)
    self.mock_client = mock.Client(
        core_apis.GetClientClass('compute', api_version),
        real_client=core_apis.GetClientInstance('compute', api_version,
                                                no_http=True))
    self.mock_client.Mock()
    self.addCleanup(self.mock_client.Unmock)
    self.track = track

  def testAddOwnerToDisk(self, track, api_version):
    self._SetUp(track, api_version)
    self.mock_client.disks.GetIamPolicy.Expect(
        self.messages.ComputeDisksGetIamPolicyRequest(
            resource='my-resource', project='fake-project', zone='zone-1'),
        response=test_resources.EmptyIamPolicy(self.messages))
    policy = test_resources.IamPolicyWithOneBinding(self.messages)
    self.mock_client.disks.SetIamPolicy.Expect(
        self.messages.ComputeDisksSetIamPolicyRequest(
            resource='my-resource', project='fake-project', zone='zone-1',
            zoneSetPolicyRequest=self.messages.ZoneSetPolicyRequest(
                bindings=policy.bindings,
                etag=policy.etag)),
        response=test_resources.IamPolicyWithOneBinding(self.messages))

    self.Run("""
        compute disks add-iam-policy-binding my-resource --zone zone-1
        --member user:testuser@google.com --role owner
        """)

    self.assertMultiLineEqual(
        self.GetOutput(),
        textwrap.dedent("""\
            bindings:
            - members:
              - user:testuser@google.com
              role: owner
            etag: dGVzdA==
            """))


if __name__ == '__main__':
  test_case.main()
