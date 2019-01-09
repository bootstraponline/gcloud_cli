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
"""Tests for the machine-types list subcommand."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.emulators import firestore_util
from googlecloudsdk.command_lib.emulators import util
from googlecloudsdk.command_lib.util import java
from tests.lib import test_case
from tests.lib.surface.compute import test_base


class FirestoreTest(test_base.BaseTest):

  def testIpv6Port(self):
    self.StartObjectPatch(
        util, 'GetHostPort', autospec=True, return_value='[::1]:12345')

    self.StartObjectPatch(java, 'RequireJavaInstalled')
    self.StartObjectPatch(util, 'EnsureComponentIsInstalled')

    ret = {}
    def SideEffect(arg):
      ret['host'] = arg.host_port.host
      ret['port'] = arg.host_port.port

    prepare_mock = self.StartObjectPatch(firestore_util, 'ValidateStartArgs')
    prepare_mock.side_effect = SideEffect
    self.StartObjectPatch(firestore_util, 'StartFirestoreEmulator')
    self.StartObjectPatch(util, 'PrefixOutput')

    self.Run('beta emulators firestore start')
    self.assertEqual('::1', ret.get('host'))
    self.assertEqual('12345', ret.get('port'))

if __name__ == '__main__':
  test_case.main()