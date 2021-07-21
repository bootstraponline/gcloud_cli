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
"""Implementation of rm command for deleting resources."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import multiprocessing

from googlecloudsdk.api_lib.storage import request_config_factory
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.storage import errors
from googlecloudsdk.command_lib.storage import flags
from googlecloudsdk.command_lib.storage import name_expansion
from googlecloudsdk.command_lib.storage import plurality_checkable_iterator
from googlecloudsdk.command_lib.storage import stdin_iterator
from googlecloudsdk.command_lib.storage.tasks import task_executor
from googlecloudsdk.command_lib.storage.tasks import task_status
from googlecloudsdk.command_lib.storage.tasks.rm import delete_task_iterator_factory
from googlecloudsdk.core import log


class Rm(base.Command):
  """Delete objects and buckets."""

  detailed_help = {
      'DESCRIPTION':
          """
      Delete objects and buckets.
      """,
      'EXAMPLES':
          """

      The following command deletes a Cloud Storage object named "my-object"
      from the bucket "my-bucket":

        $ {command} gs://my-bucket/my-object

      The following command deletes all objects directly within the directory
      "my-dir" but no objects within subdirectories:

        $ {command} gs://my-bucket/my-dir/*

      The following command deletes all objects and subdirectories within the
      directory "my-dir":

        $ {command} gs://my-bucket/my-dir/**

      Note that for buckets that contain
      [versioned objects](https://cloud.google.com/storage/docs/object-versioning),
      the above command only affects live versions. Use the `--recursive` flag
      instead to delete all versions.

      The following command deletes all versions of all resources in
      "my-bucket" and then deletes the bucket.

        $ {command} --recursive gs://my-bucket/

      The following command deletes all text files in the top-level of
      "my-bucket", but not text files in subdirectories:

        $ {command} -recursive gs://my-bucket/*.txt

      The following command deletes one wildcard expression per line passed
      in by stdin:

        $ some_program | {command} -I
      """,
  }

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'urls',
        nargs='*',
        help='The URLs of the resources to delete.')
    parser.add_argument(
        '--stdin',
        '-I',
        action='store_true',
        help='Read the list of resources to remove from stdin.')
    parser.add_argument(
        '--recursive',
        '-R',
        '-r',
        action='store_true',
        help=('Recursively delete the contents of buckets or directories that'
              ' match the path expression. If the path is set to a bucket, like'
              ' ``gs://bucket\'\', the bucket is also deleted. This option'
              ' implies the `--all-versions` option. If you want to delete only'
              ' live object versions, use the ``**\'\' wildcard instead.'))
    parser.add_argument(
        '--all-versions',
        '-a',
        action='store_true',
        help='Delete all'
        ' [versions](https://cloud.google.com/storage/docs/object-versioning)'
        ' of an object.')

    flags.add_precondition_flags(parser)

  def Run(self, args):
    if args.stdin:
      if args.urls:
        raise errors.Error(
            'No URL arguments allowed when reading URLs from stdin.')
      urls = stdin_iterator.StdinIterator()
    else:
      if not args.urls:
        raise errors.Error(
            'Without the --stdin flag, the rm command requires at least one URL'
            ' argument.')
      urls = args.urls

    name_expansion_iterator = name_expansion.NameExpansionIterator(
        urls,
        all_versions=args.all_versions or args.recursive,
        include_buckets=args.recursive,
        recursion_requested=args.recursive)

    user_request_args = request_config_factory.get_user_request_args_from_command_args(
        args)
    task_status_queue = multiprocessing.Queue()
    task_iterator_factory = (
        delete_task_iterator_factory.DeleteTaskIteratorFactory(
            name_expansion_iterator,
            task_status_queue=task_status_queue,
            user_request_args=user_request_args))

    log.status.Print('Removing objects:')
    task_executor.execute_tasks(
        task_iterator_factory.object_iterator(),
        parallelizable=True,
        task_status_queue=task_status_queue,
        progress_type=task_status.ProgressType.COUNT)

    bucket_iterator = plurality_checkable_iterator.PluralityCheckableIterator(
        task_iterator_factory.bucket_iterator())

    # We perform the is_empty check to avoid printing unneccesary status lines.
    if args.recursive and not bucket_iterator.is_empty():
      log.status.Print('Removing Buckets:')
      task_executor.execute_tasks(
          bucket_iterator,
          parallelizable=True,
          task_status_queue=task_status_queue,
          progress_type=task_status.ProgressType.COUNT)
