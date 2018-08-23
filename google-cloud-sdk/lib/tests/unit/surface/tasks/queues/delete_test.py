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
"""Tests for `gcloud tasks queues delete`."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.tasks import app
from googlecloudsdk.command_lib.tasks import constants
from googlecloudsdk.command_lib.tasks import parsers
from googlecloudsdk.core.console import console_io
from tests.lib import test_case
from tests.lib.apitools import http_error
from tests.lib.surface.tasks import test_base


class QueuesDeleteTest(test_base.CloudTasksTestBase, test_case.WithInput):

  def SetUp(self):
    self.resolve_loc_mock = self.StartObjectPatch(app, 'ResolveAppLocation')
    self.resolve_loc_mock.return_value = (
        parsers.ParseLocation('us-central1').SelfLink())

  def testDelete(self):
    self.queues_service.Delete.Expect(
        self.messages.CloudtasksProjectsLocationsQueuesDeleteRequest(
            name='projects/{}/locations/us-central1/queues/{}'.format(
                self.Project(), 'my-queue')),
        response=self.messages.Empty())
    self.WriteInput('Y')

    output = self.Run('tasks queues delete my-queue')

    self.assertIsNone(output)
    self.AssertErrContains(constants.QUEUE_MANAGEMENT_WARNING)
    self.AssertErrContains('Deleted queue [my-queue].')

  def testDelete_RelativeName(self):
    queue_name = 'projects/other-project/locations/us-central1/queues/my-queue'
    self.queues_service.Delete.Expect(
        self.messages.CloudtasksProjectsLocationsQueuesDeleteRequest(
            name=queue_name),
        response=self.messages.Empty())
    self.WriteInput('Y')

    self.Run('tasks queues delete {}'.format(queue_name))
    self.AssertErrContains(constants.QUEUE_MANAGEMENT_WARNING)

  def testDelete_NoApp(self):
    self.resolve_loc_mock.side_effect = app.RegionResolvingError

    with self.assertRaises(app.RegionResolvingError):
      self.Run('tasks queues delete my-queue')

  def testDelete_NonExistentQueue(self):
    self.queues_service.Delete.Expect(
        self.messages.CloudtasksProjectsLocationsQueuesDeleteRequest(
            name='projects/{}/locations/us-central1/queues/{}'.format(
                self.Project(), 'my-queue')),
        exception=http_error.MakeDetailedHttpError(
            code=404,
            message='Requested entity was not found.'))
    self.WriteInput('Y')

    with self.assertRaises(exceptions.HttpException):
      self.Run('tasks queues delete my-queue')

    self.AssertErrNotContains('Deleted queue [my-queue].')
    self.AssertErrContains(constants.QUEUE_MANAGEMENT_WARNING)
    self.AssertErrContains('Requested entity was not found.')

  def testDelete_Cancel(self):
    self.WriteInput('N')

    with self.assertRaises(console_io.OperationCancelledError):
      self.Run('tasks queues delete my-queue')

  def testDelete_Location(self):
    self.queues_service.Delete.Expect(
        self.messages.CloudtasksProjectsLocationsQueuesDeleteRequest(
            name='projects/{}/locations/us-central2/queues/{}'.format(
                self.Project(), 'my-queue')),
        response=self.messages.Empty())
    self.WriteInput('Y')

    output = self.Run('tasks queues delete my-queue --location=us-central2')

    self.assertIsNone(output)
    self.AssertErrContains(constants.QUEUE_MANAGEMENT_WARNING)
    self.AssertErrContains('Deleted queue [my-queue].')


if __name__ == '__main__':
  test_case.main()
