# -*- coding: utf-8 -*- #
# Copyright 2016 Google Inc. All Rights Reserved.
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
"""Tests that exercise user creation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.util import apis
from tests.lib import test_case
from tests.lib.surface.sql import base


class _BaseUsersCreateTest(object):

  # TODO(b/110486599): Remove the positional host argument.
  def testCreate(self):
    msgs = apis.GetMessagesModule('sqladmin', 'v1beta4')
    self.mocked_client.users.Insert.Expect(
        msgs.User(
            project=self.Project(),
            instance='my_instance',
            name='my_username',
            host='my_host',
            password='my_password'),
        msgs.Operation(name='op_name'))
    self.mocked_client.operations.Get.Expect(
        msgs.SqlOperationsGetRequest(
            operation='op_name', project=self.Project()),
        msgs.Operation(name='op_name', status='DONE'))
    self.Run('sql users create --instance my_instance '
             'my_username my_host --password my_password')
    self.AssertOutputEquals('')
    self.AssertErrContains('Creating Cloud SQL user')
    self.AssertErrContains('Created user [my_username].')
    # TODO(b/110486599): Remove the deprecation warning.
    self.AssertErrContains('Positional argument deprecated_host is deprecated')

  def testCreateWithNoHostArgument(self):
    msgs = apis.GetMessagesModule('sqladmin', 'v1beta4')
    self.mocked_client.users.Insert.Expect(
        msgs.User(
            project=self.Project(),
            instance='my_instance',
            name='my_username',
            host=None,
            password='my_password'),
        msgs.Operation(name='op_name'))
    self.mocked_client.operations.Get.Expect(
        msgs.SqlOperationsGetRequest(
            operation='op_name', project=self.Project()),
        msgs.Operation(name='op_name', status='DONE'))
    self.Run('sql users create --instance my_instance '
             'my_username --password my_password')
    self.AssertOutputEquals('')
    self.AssertErrContains('Creating Cloud SQL user')
    self.AssertErrContains('Created user [my_username].')

  def testCreateWithHostFlag(self):
    msgs = apis.GetMessagesModule('sqladmin', 'v1beta4')
    self.mocked_client.users.Insert.Expect(
        msgs.User(
            project=self.Project(),
            instance='my_instance',
            name='my_username',
            host='my_host',
            password='my_password'),
        msgs.Operation(name='op_name'))
    self.mocked_client.operations.Get.Expect(
        msgs.SqlOperationsGetRequest(
            operation='op_name', project=self.Project()),
        msgs.Operation(name='op_name', status='DONE'))
    self.Run('sql users create --instance my_instance '
             'my_username --host my_host --password my_password')
    self.AssertOutputEquals('')
    self.AssertErrContains('Creating Cloud SQL user')
    self.AssertErrContains('Created user [my_username].')

  # TODO(b/110486599): Remove the positional host argument.
  def testCreateAsync(self):
    msgs = apis.GetMessagesModule('sqladmin', 'v1beta4')
    self.mocked_client.users.Insert.Expect(
        msgs.User(
            project=self.Project(),
            instance='my_instance',
            name='my_username',
            host='my_host',
            password='my_password'),
        msgs.Operation(name='op_name'))
    self.mocked_client.operations.Get.Expect(
        msgs.SqlOperationsGetRequest(
            operation='op_name', project=self.Project()),
        msgs.Operation(name='op_name'))
    result = self.Run('sql users create --instance my_instance '
                      'my_username my_host --password my_password --async')
    self.assertEqual(result.name, 'op_name')
    self.AssertOutputEquals('')
    self.AssertErrContains('Create in progress for user [my_username].\n')


class UsersCreateGATest(_BaseUsersCreateTest, base.SqlMockTestGA):
  pass


class UsersCreateBetaTest(_BaseUsersCreateTest, base.SqlMockTestBeta):
  pass


class UsersCreateAlphaTest(_BaseUsersCreateTest, base.SqlMockTestAlpha):
  pass


if __name__ == '__main__':
  test_case.main()
