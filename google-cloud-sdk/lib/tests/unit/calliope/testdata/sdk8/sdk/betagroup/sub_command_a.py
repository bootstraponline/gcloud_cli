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
"""gcloud sdk tests command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.util import completers

from six.moves import range  # pylint: disable=redefined-builtin


class BetaSubCommandA(base.Command):
  """gcloud sdk tests command."""

  @staticmethod
  def Args(parser):
    """Adds args for this command."""

    # Choices.
    parser.add_argument(
        '--one-two-three',
        choices=list(range(1, 4)),
        type=int,
        help='...four!')

    # Resource.
    parser.add_argument(
        '--resourceful',
        completer=completers.NoCacheCompleter,
        help='Resource Arg')

