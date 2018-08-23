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

"""Test of the 'pubsub topics add-iam-policy-binding' command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.pubsub import util
from tests.lib import test_case
from tests.lib.surface.pubsub import base


class TopicsAddIamPolicyBindingTest(base.CloudPubsubTestBase):

  def SetUp(self):
    self.svc = self.client.projects_topics

  def testAddIamPolicyBinding(self):
    topic_ref = util.ParseTopic('topic1', self.Project())
    new_role = 'roles/pubsub.publisher'
    new_member = 'user:foo@google.com'
    policy = self.msgs.Policy(
        bindings=[
            self.msgs.Binding(
                role=new_role,
                members=['user:bar@google.com']),
            self.msgs.Binding(
                role='roles/pubsub.editor',
                members=['users:admin@google.com'])
        ],
        etag=b'unique_tag',
        version=1)

    new_policy = self.msgs.Policy(
        bindings=[
            self.msgs.Binding(
                role=new_role,
                members=['user:bar@google.com', new_member]),
            self.msgs.Binding(
                role='roles/pubsub.editor',
                members=['users:admin@google.com'])
        ],
        etag=b'unique_tag',
        version=1)

    self.svc.GetIamPolicy.Expect(
        self.msgs.PubsubProjectsTopicsGetIamPolicyRequest(
            resource=topic_ref.RelativeName()),
        policy)
    self.svc.SetIamPolicy.Expect(
        self.msgs.PubsubProjectsTopicsSetIamPolicyRequest(
            resource=topic_ref.RelativeName(),
            setIamPolicyRequest=self.msgs.SetIamPolicyRequest(
                policy=new_policy)),
        new_policy)

    result = self.Run(
        'pubsub topics add-iam-policy-binding topic1 '
        '--role {} --member {}'.format(new_role, new_member))

    self.assertEqual(result, new_policy)


if __name__ == '__main__':
  test_case.main()
