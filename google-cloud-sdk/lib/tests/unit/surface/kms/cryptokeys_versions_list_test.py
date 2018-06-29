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
"""Tests that exercise the 'gcloud kms cryptokeys versions list' command."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.calliope import base as calliope_base
from googlecloudsdk.calliope.base import DeprecationException
from tests.lib import parameterized
from tests.lib import test_case
from tests.lib.surface.kms import base


@parameterized.parameters(calliope_base.ReleaseTrack.ALPHA,
                          calliope_base.ReleaseTrack.BETA,
                          calliope_base.ReleaseTrack.GA)
class CryptokeysVersionsListTest(base.KmsMockTest):

  def testList(self, track):
    self.track = track
    version_1 = self.project_name.Descendant('global/my_kr/my_key/1')

    with self.assertRaises(DeprecationException):
      self.Run('kms cryptokeys versions list --location={0} --keyring {1} '
               '--key {2}'.format(version_1.location_id, version_1.
                                  key_ring_id, version_1.crypto_key_id))


if __name__ == '__main__':
  test_case.main()
