# -*- coding: utf-8 -*- #
# Copyright 2017 Google Inc. All Rights Reserved.
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

"""Unit tests for endpoints services remove-iam-policy-binding command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import base64

from googlecloudsdk.api_lib.endpoints import services_util

from tests.lib import test_case
from tests.lib.surface.endpoints import unit_test_base

# Shorten the Access Policy Get request name for better readability
GET_REQUEST = (services_util.GetMessagesModule()
               .ServicemanagementServicesGetIamPolicyRequest)


class EndpointsRemoveIamPolicyBindingTest(unit_test_base.EV1UnitTestBase):
  """Unit tests for endpoints services remove-iam-policy-binding command."""

  def PreSetUp(self):
    self.access_policy_msg = self.services_messages.Policy
    self.etag = b'test_etag'
    self.encoded_etag = base64.b64encode(self.etag).strip()
    self.consumer_role = 'roles/servicemanagement.serviceConsumer'

  def testRemoveUserFromService(self):
    extant_emails = ['u1@google.com', 'u2@google.com']
    extant_members = ['user:%s' % e for e in extant_emails]
    member_to_remove = extant_members[0]
    remaining_member = extant_members[1]

    old_policy = self.access_policy_msg(
        bindings=[self.services_messages.Binding(role=self.consumer_role,
                                                 members=extant_members)],
        etag=self.etag
    )

    new_policy = self.access_policy_msg(
        bindings=[self.services_messages.Binding(
            role=self.consumer_role, members=[remaining_member])],
        etag=self.etag
    )

    self.mocked_client.services.GetIamPolicy.Expect(
        request=GET_REQUEST(servicesId=self.DEFAULT_SERVICE_NAME),
        response=old_policy
    )

    set_policy_request = self.services_messages.SetIamPolicyRequest(
        policy=new_policy)
    expected_request = (self.services_messages.
                        ServicemanagementServicesSetIamPolicyRequest(
                            servicesId=self.DEFAULT_SERVICE_NAME,
                            setIamPolicyRequest=set_policy_request))

    self.mocked_client.services.SetIamPolicy.Expect(
        request=expected_request,
        response=new_policy)

    response = self.Run(
        'endpoints services remove-iam-policy-binding {0} --member {1} '
        '--role {2}'.format(self.DEFAULT_SERVICE_NAME,
                            member_to_remove,
                            self.consumer_role))
    self.assertEqual(response, new_policy)

  def testServicesAccessRemoveGroupFromService(self):
    extant_emails = ['g1@google.com', 'u1@google.com']
    extant_members = ['%s:%s' % ('user' if e[0] == 'u' else 'group', e)
                      for e in extant_emails]
    member_to_remove = extant_members[0]
    remaining_member = extant_members[1]

    old_policy = self.access_policy_msg(
        bindings=[self.services_messages.Binding(role=self.consumer_role,
                                                 members=extant_members)],
        etag=self.etag
    )

    new_policy = self.access_policy_msg(
        bindings=[self.services_messages.Binding(
            role=self.consumer_role, members=[remaining_member])],
        etag=self.etag
    )

    self.mocked_client.services.GetIamPolicy.Expect(
        request=GET_REQUEST(servicesId=self.DEFAULT_SERVICE_NAME),
        response=old_policy
    )

    set_policy_request = self.services_messages.SetIamPolicyRequest(
        policy=new_policy)
    expected_request = (self.services_messages.
                        ServicemanagementServicesSetIamPolicyRequest(
                            servicesId=self.DEFAULT_SERVICE_NAME,
                            setIamPolicyRequest=set_policy_request))

    self.mocked_client.services.SetIamPolicy.Expect(
        request=expected_request,
        response=new_policy)

    response = self.Run(
        'endpoints services remove-iam-policy-binding {0} --member {1} '
        '--role {2}'.format(self.DEFAULT_SERVICE_NAME,
                            member_to_remove,
                            self.consumer_role))
    self.assertEqual(response, new_policy)

  def testServicesAccessRemoveAllUsersFromService(self):
    member = 'allUsers'

    old_policy = self.access_policy_msg(
        bindings=[self.services_messages.Binding(
            role=self.consumer_role, members=[member])],
        etag=self.etag
    )

    new_policy = self.access_policy_msg(bindings=[], etag=self.etag)

    self.mocked_client.services.GetIamPolicy.Expect(
        request=GET_REQUEST(servicesId=self.DEFAULT_SERVICE_NAME),
        response=old_policy
    )

    set_policy_request = self.services_messages.SetIamPolicyRequest(
        policy=new_policy)
    expected_request = (self.services_messages.
                        ServicemanagementServicesSetIamPolicyRequest(
                            servicesId=self.DEFAULT_SERVICE_NAME,
                            setIamPolicyRequest=set_policy_request))

    self.mocked_client.services.SetIamPolicy.Expect(
        request=expected_request,
        response=new_policy)

    response = self.Run(
        'endpoints services remove-iam-policy-binding {0} --member {1} '
        '--role {2}'.format(self.DEFAULT_SERVICE_NAME,
                            member,
                            self.consumer_role))
    self.assertEqual(response, new_policy)


if __name__ == '__main__':
  test_case.main()
