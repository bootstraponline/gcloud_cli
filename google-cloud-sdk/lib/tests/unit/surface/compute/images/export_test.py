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
"""Tests for the images export subcommand."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import encoding
from apitools.base.py.testing import mock

from googlecloudsdk.api_lib.util import apis as core_apis
from googlecloudsdk.core import properties
from tests.lib import e2e_base
from tests.lib import sdk_test_base
from tests.lib import test_case

_DEFAULT_TIMEOUT = '7056s'


class ImagesExportTest(e2e_base.WithMockHttp, sdk_test_base.SdkBase):

  def SetUp(self):
    self.mocked_cloudbuild_v1 = mock.Client(
        core_apis.GetClientClass('cloudbuild', 'v1'),
    )
    self.mocked_cloudbuild_v1.Mock()
    self.addCleanup(self.mocked_cloudbuild_v1.Unmock)
    self.cloudbuild_v1_messages = core_apis.GetMessagesModule(
        'cloudbuild', 'v1')

    self.mocked_storage_v1 = mock.Client(
        core_apis.GetClientClass('storage', 'v1'))
    self.mocked_storage_v1.Mock()
    self.addCleanup(self.mocked_storage_v1.Unmock)
    self.storage_v1_messages = core_apis.GetMessagesModule(
        'storage', 'v1')

    self.mocked_crm_v1 = mock.Client(
        core_apis.GetClientClass('cloudresourcemanager', 'v1'))
    self.mocked_crm_v1.Mock()
    self.addCleanup(self.mocked_crm_v1.Unmock)
    self.crm_v1_messages = core_apis.GetMessagesModule(
        'cloudresourcemanager', 'v1')

    self.mocked_servicemanagement_v1 = mock.Client(
        core_apis.GetClientClass('servicemanagement', 'v1'))
    self.mocked_servicemanagement_v1.Mock()
    self.addCleanup(self.mocked_servicemanagement_v1.Unmock)
    self.servicemanagement_v1_messages = core_apis.GetMessagesModule(
        'servicemanagement', 'v1')

    properties.VALUES.core.project.Set('my-project')
    self._statuses = self.cloudbuild_v1_messages.Build.StatusValueValuesEnum

    self.image_name = 'my-image'
    self.destination_uri = 'gs://my-bucket/my-image.tar.gz'
    self.daisy_builder = 'gcr.io/compute-image-tools/daisy:release'

    self.project = self.crm_v1_messages.Project(
        projectId='my-project', projectNumber=123456)
    admin_permissions_binding = self.crm_v1_messages.Binding(
        members=['serviceAccount:123456@cloudbuild.gserviceaccount.com'],
        role='roles/compute.admin')
    iam_permissions_binding = self.crm_v1_messages.Binding(
        members=['serviceAccount:123456@cloudbuild.gserviceaccount.com'],
        role='roles/iam.serviceAccountActor')
    self.permissions = self.crm_v1_messages.Policy(
        bindings=[admin_permissions_binding, iam_permissions_binding])
    self.services = self.servicemanagement_v1_messages.ListServicesResponse(
        services=[self.servicemanagement_v1_messages.ManagedService(
            serviceName='cloudbuild.googleapis.com')]
    )

  def PrepareMocks(self, daisy_step):
    buildin = self.cloudbuild_v1_messages.Build(
        steps=[daisy_step],
        tags=['gce-daisy', 'gce-daisy-image-export'],
        timeout='7200s',
    )

    buildout = self.cloudbuild_v1_messages.Build(
        id='1234',
        projectId='my-project',
        steps=[daisy_step],
        tags=['gce-daisy', 'gce-daisy-image-export'],
        status=self._statuses.SUCCESS,
        logsBucket='gs://my-project_cloudbuild/logs',
        timeout='7200s',
    )
    op_metadata = self.cloudbuild_v1_messages.BuildOperationMetadata(
        build=buildout,
    )

    self.AddHTTPResponse(
        'https://storage.googleapis.com/my-project_cloudbuild/'
        'logs/log-1234.txt',
        request_headers={'Range': 'bytes=0-'}, status=200,
        body='Cloudbuild output\n[image-export] output\n')

    self.mocked_servicemanagement_v1.services.List.Expect(
        self.servicemanagement_v1_messages.ServicemanagementServicesListRequest(
            consumerId='project:my-project',
            pageSize=100,
        ),
        response=self.services,
    )

    self.mocked_cloudbuild_v1.projects_builds.Create.Expect(
        self.cloudbuild_v1_messages.CloudbuildProjectsBuildsCreateRequest(
            build=buildin,
            projectId='my-project',
        ),
        response=self.cloudbuild_v1_messages.Operation(
            metadata=encoding.JsonToMessage(
                self.cloudbuild_v1_messages.Operation.MetadataValue,
                encoding.MessageToJson(op_metadata)))
    )

    self.mocked_cloudbuild_v1.projects_builds.Get.Expect(
        self.cloudbuild_v1_messages.CloudbuildProjectsBuildsGetRequest(
            id='1234',
            projectId='my-project',
        ),
        response=buildout,
    )

    self.mocked_crm_v1.projects.Get.Expect(
        self.crm_v1_messages.CloudresourcemanagerProjectsGetRequest(
            projectId='my-project',
        ),
        response=self.project,
    )

    self.mocked_crm_v1.projects.GetIamPolicy.Expect(
        self.crm_v1_messages.CloudresourcemanagerProjectsGetIamPolicyRequest(
            resource='my-project',
        ),
        response=self.permissions,
    )

    self.mocked_storage_v1.buckets.Insert.Expect(
        self.storage_v1_messages.StorageBucketsInsertRequest(
            bucket=self.storage_v1_messages.Bucket(
                name='my-project-daisy-bkt'),
            project='my-project',
        ),
        response='foo',
    )

  def testCommonCase(self):
    export_workflow = ('../workflows/export/image_export.wf.json')
    daisy_step = self.cloudbuild_v1_messages.BuildStep(
        args=['-gcs_path=gs://my-project-daisy-bkt/',
              '-default_timeout={0}'.format(_DEFAULT_TIMEOUT),
              '-variables=source_image=projects/my-project/global/images/{0},'
              'destination={1}'
              .format(self.image_name, self.destination_uri),
              export_workflow,],
        name=self.daisy_builder,
    )

    self.PrepareMocks(daisy_step)

    self.Run("""
             compute images export --image {0}
             --destination-uri {1}
             """.format(self.image_name, self.destination_uri))

    self.AssertOutputContains("""\
        [image-export] output
        """, normalize_space=True)

  def testExportFormat(self):
    export_workflow = ('../workflows/export/image_export_ext.wf.json')
    daisy_step = self.cloudbuild_v1_messages.BuildStep(
        args=['-gcs_path=gs://my-project-daisy-bkt/',
              '-default_timeout={0}'.format(_DEFAULT_TIMEOUT),
              '-variables=source_image=projects/my-project/global/images/{0},'
              'destination={1},format=vmdk'
              .format(self.image_name, self.destination_uri),
              export_workflow,],
        name=self.daisy_builder,
    )

    self.PrepareMocks(daisy_step)

    self.Run("""
             compute images export --image {0}
             --destination-uri {1} --export-format=vmdk
             """.format(self.image_name, self.destination_uri))

    self.AssertOutputContains("""\
        [image-export] output
        """, normalize_space=True)

  def testZoneFlag(self):
    zone = 'us-west1-c'
    export_workflow = ('../workflows/export/image_export.wf.json')
    daisy_step = self.cloudbuild_v1_messages.BuildStep(
        args=['-zone={0}'.format(zone),
              '-gcs_path=gs://my-project-daisy-bkt/',
              '-default_timeout={0}'.format(_DEFAULT_TIMEOUT),
              '-variables=source_image=projects/my-project/global/images/{0},'
              'destination={1}'
              .format(self.image_name, self.destination_uri),
              export_workflow,],
        name=self.daisy_builder,
    )

    self.PrepareMocks(daisy_step)

    self.Run("""
             compute images export --image {0}
             --destination-uri {1} --zone={2}
             """.format(self.image_name, self.destination_uri, zone))

    self.AssertOutputContains("""\
        [image-export] output
        """, normalize_space=True)

  def testImageProject(self):
    export_workflow = ('../workflows/export/image_export.wf.json')
    daisy_step = self.cloudbuild_v1_messages.BuildStep(
        args=['-gcs_path=gs://my-project-daisy-bkt/',
              '-default_timeout={0}'.format(_DEFAULT_TIMEOUT),
              '-variables=source_image=projects/debian-cloud/global/images/{0},'
              'destination={1}'
              .format(self.image_name, self.destination_uri),
              export_workflow,],
        name=self.daisy_builder,
    )

    self.PrepareMocks(daisy_step)

    self.Run("""
             compute images export --image {0}
             --destination-uri {1} --image-project debian-cloud
             """.format(self.image_name, self.destination_uri))

    self.AssertOutputContains("""\
        [image-export] output
        """, normalize_space=True)

  def testNetworkFlag(self):
    export_workflow = ('../workflows/export/image_export.wf.json')
    daisy_step = self.cloudbuild_v1_messages.BuildStep(
        args=['-gcs_path=gs://my-project-daisy-bkt/',
              '-default_timeout={0}'.format(_DEFAULT_TIMEOUT),
              '-variables=source_image=projects/my-project/global/images/{0},'
              'destination={1},export_network=global/networks/my-network'
              .format(self.image_name, self.destination_uri),
              export_workflow,],
        name=self.daisy_builder,
    )

    self.PrepareMocks(daisy_step)

    self.Run("""
             compute images export --image {0}
             --destination-uri {1} --network my-network
             """.format(self.image_name, self.destination_uri))

    self.AssertOutputContains("""\
        [image-export] output
        """, normalize_space=True)

  def testMissingImage(self):
    with self.AssertRaisesArgumentErrorMatches(
        'Exactly one of (--image | --image-family) must be specified.'):
      self.Run("""
               compute images export --destination-uri {0}
               """.format(self.destination_uri))

  def testMissingDestination(self):
    with self.AssertRaisesArgumentErrorMatches(
        'argument --destination-uri: Must be specified'):
      self.Run("""
               compute images export --image {0}
               """.format(self.image_name))

if __name__ == '__main__':
  test_case.main()
