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
"""Deletes a backend binding of a KubeRun service."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.kuberun import flags
from googlecloudsdk.command_lib.kuberun import kuberun_command
from googlecloudsdk.core import log

_DETAILED_HELP = {
    'EXAMPLES':
        """
        To delete a backend binding in the default namespace, i.e. remove its
        target KubeRun service from the backends list of a Compute Engine
        backend service, run:

            $ {command} BACKEND_SERVICE
        """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Delete(kuberun_command.KubeRunCommand, base.DeleteCommand):
  """Deletes a backend binding."""

  detailed_help = _DETAILED_HELP
  flags = [flags.NamespaceFlag(), flags.ClusterConnectionFlags()]

  @classmethod
  def Args(cls, parser):
    super(Delete, cls).Args(parser)
    parser.add_argument(
        'backend_binding',
        help="""Backend binding to delete. Its name is the same as the
        Compute Engine backend service it's bound to.""")

  def BuildKubeRunArgs(self, args):
    return [args.backend_binding] + super(Delete, self).BuildKubeRunArgs(args)

  def Command(self):
    return ['core', 'backend-bindings', 'delete']

  def OperationResponseHandler(self, response, args):
    super(Delete, self).OperationResponseHandler(response, args)
    log.DeletedResource(args.backend_binding, 'backend binding')
    return None
