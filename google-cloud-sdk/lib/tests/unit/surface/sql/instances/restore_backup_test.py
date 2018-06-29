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
"""Tests that exercise operations listing and executing."""

from __future__ import absolute_import
from __future__ import unicode_literals
import datetime

from apitools.base.protorpclite import util as protorpc_util
from apitools.base.py.testing import mock

from googlecloudsdk.api_lib.util import apis as core_apis
from tests.lib import test_case
from tests.lib.surface.sql import base

sqladmin_v1beta3 = core_apis.GetMessagesModule('sqladmin', 'v1beta3')


class InstancesRestoreBackupTest(base.SqlMockTestBeta):
  # pylint:disable=g-tzinfo-datetime

  def _ExpectRestoreBackup(self):
    self.mocked_client.instances.RestoreBackup.Expect(
        self.messages.SqlInstancesRestoreBackupRequest(
            # pylint:disable=line-too-long
            instance='clone-instance-7',
            project=self.Project(),
            instancesRestoreBackupRequest=self.messages.
            InstancesRestoreBackupRequest(
                restoreBackupContext=self.messages.RestoreBackupContext(
                    backupRunId=1438876800422,
                    instanceId='clone-instance-7',
                ),),
        ),
        self.messages.Operation(
            # pylint:disable=line-too-long
            insertTime=datetime.datetime(
                2014,
                8,
                12,
                19,
                38,
                39,
                415000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            startTime=None,
            endTime=None,
            error=None,
            exportContext=None,
            importContext=None,
            targetId='clone-instance-7',
            targetLink=
            'https://www.googleapis.com/sql/v1beta4/projects/{0}/instances/clone-instance-7'.
            format(self.Project()),
            targetProject=self.Project(),
            kind='sql#operation',
            name='1178746b-14d4-4258-bbdd-52856882c213',
            selfLink=
            'https://www.googleapis.com/sql/v1beta4/projects/{0}/operations/1178746b-14d4-4258-bbdd-52856882c213'.
            format(self.Project()),
            operationType='RESTORE_VOLUME',
            status='PENDING',
            user='170350250316@developer.gserviceaccount.com',
        ))
    self.mocked_client.operations.Get.Expect(
        self.messages.SqlOperationsGetRequest(
            operation='1178746b-14d4-4258-bbdd-52856882c213',
            project=self.Project(),
        ),
        self.messages.Operation(
            # pylint:disable=line-too-long
            insertTime=datetime.datetime(
                2014,
                8,
                12,
                19,
                38,
                39,
                415000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            startTime=datetime.datetime(
                2014,
                8,
                12,
                19,
                38,
                39,
                525000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            endTime=datetime.datetime(
                2014,
                8,
                12,
                19,
                39,
                26,
                601000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            error=None,
            exportContext=None,
            importContext=None,
            targetId='clone-instance-7',
            targetLink=
            'https://www.googleapis.com/sql/v1beta4/projects/{0}/instances/clone-instance-7'.
            format(self.Project()),
            targetProject=self.Project(),
            kind='sql#operation',
            name='1178746b-14d4-4258-bbdd-52856882c213',
            selfLink=
            'https://www.googleapis.com/sql/v1beta4/projects/{0}/operations/1178746b-14d4-4258-bbdd-52856882c213'.
            format(self.Project()),
            operationType='RESTORE_VOLUME',
            status='DONE',
            user='170350250316@developer.gserviceaccount.com',
        ))

  def testRestoreBackup(self):
    self._ExpectRestoreBackup()

    self.Run('sql instances restore-backup clone-instance-7 '
             '--backup-id=1438876800422')
    self.AssertErrContains(
        'Restored [https://www.googleapis.com/sql/v1beta4/'
        'projects/{0}/instances/clone-instance-7].'.format(self.Project()))

  def testRestoreBackupAsync(self):
    self._ExpectRestoreBackup()

    self.Run('sql instances restore-backup clone-instance-7 '
             '--backup-id=1438876800422 --async')
    self.AssertErrNotContains(
        'Restored [https://www.googleapis.com/sql/v1beta4/'
        'projects/{0}/instances/clone-instance-7].'.format(self.Project()))

  def _ExpectRestoreBackupV1Beta3(self):
    self.mocked_client_v1beta3 = mock.Client(
        core_apis.GetClientClass('sql', 'v1beta3'))
    self.mocked_client_v1beta3.Mock()
    self.addCleanup(self.mocked_client_v1beta3.Unmock)
    self.mocked_client_v1beta3.instances.Get.Expect(
        sqladmin_v1beta3.SqlInstancesGetRequest(
            instance='clone-instance-7',
            project=self.Project(),
        ),
        sqladmin_v1beta3.DatabaseInstance(
            currentDiskSize=287592724,
            databaseVersion='MYSQL_5_5',
            etag='"DExdZ69FktjWMJ-ohD1vLZW9pnk/NA"',
            instance='clone-instance-7',
            ipAddresses=[],
            kind='sql#instance',
            maxDiskSize=268435456000,
            project=self.Project(),
            region='us-central',
            serverCaCert=sqladmin_v1beta3.SslCert(
                cert='-----BEGIN CERTIFICATE-----\nMIIDITCCAgmgAwIBAgIBADANBg',
                certSerialNumber='0',
                commonName='C=US,O=Google\\, Inc,CN=Google Cloud SQL Server C',
                createTime=datetime.datetime(
                    2014,
                    8,
                    13,
                    21,
                    47,
                    29,
                    512000,
                    tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
                expirationTime=datetime.datetime(
                    2024,
                    8,
                    10,
                    21,
                    47,
                    29,
                    512000,
                    tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
                instance='clone-instance-7',
                kind='sql#sslCert',
                sha1Fingerprint='2dbfcefd3c962a284035ffb06dccdd2055d32b46',
            ),
            settings=sqladmin_v1beta3.Settings(
                activationPolicy='ON_DEMAND',
                authorizedGaeApplications=[],
                backupConfiguration=[
                    sqladmin_v1beta3.BackupConfiguration(
                        binaryLogEnabled=True,
                        enabled=True,
                        id='43ee7461-d2d8-4c5b-8d8e-98fa3f9d2ecc',
                        kind='sql#backupConfiguration',
                        startTime='23:00',
                    ),
                ],
                databaseFlags=[],
                ipConfiguration=sqladmin_v1beta3.IpConfiguration(
                    authorizedNetworks=[],
                    enabled=False,
                    requireSsl=None,
                ),
                kind='sql#settings',
                locationPreference=None,
                pricingPlan='PER_USE',
                replicationType='SYNCHRONOUS',
                settingsVersion=4,
                tier='D1',
            ),
            state='RUNNABLE',
        ))
    self.mocked_client_v1beta3.instances.RestoreBackup.Expect(
        sqladmin_v1beta3.SqlInstancesRestoreBackupRequest(
            backupConfiguration='43ee7461-d2d8-4c5b-8d8e-98fa3f9d2ecc',
            dueTime='2014-08-13T23:00:00.802000+00:00',
            instance='clone-instance-7',
            project=self.Project(),
        ),
        sqladmin_v1beta3.InstancesRestoreBackupResponse(
            kind='sql#instancesRestoreBackup',
            operation='7e3d8e00-9300-4baa-8f58-5b429b9b5fd1',
        ))
    self.mocked_client_v1beta3.operations.Get.Expect(
        sqladmin_v1beta3.SqlOperationsGetRequest(
            instance='clone-instance-7',
            operation='7e3d8e00-9300-4baa-8f58-5b429b9b5fd1',
            project=self.Project(),
        ),
        sqladmin_v1beta3.InstanceOperation(
            endTime=datetime.datetime(
                2014,
                8,
                14,
                21,
                47,
                41,
                505000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            enqueuedTime=datetime.datetime(
                2014,
                8,
                14,
                21,
                46,
                35,
                146000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            error=[],
            exportContext=None,
            importContext=None,
            instance='clone-instance-7',
            kind='sql#instanceOperation',
            operation='7e3d8e00-9300-4baa-8f58-5b429b9b5fd1',
            operationType='RESTORE_VOLUME',
            startTime=datetime.datetime(
                2014,
                8,
                14,
                21,
                46,
                35,
                195000,
                tzinfo=protorpc_util.TimeZoneOffset(datetime.timedelta(0))),
            state='DONE',
            userEmailAddress='170350250316@developer.gserviceaccount.com',
        ))


if __name__ == '__main__':
  test_case.main()
