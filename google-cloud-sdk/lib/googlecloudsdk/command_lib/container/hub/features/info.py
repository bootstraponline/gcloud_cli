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
"""Unified information for working with various features."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


class Info(object):
  """Info contains information about a given Feature.

  Attributes:
    display_name: The Feature name as it should be displayed to users.
    api: The API associated with this Feature (for enablement).
    cmd_group: The subgroup for this Feature, e.g. `container hub <cmd_group`.
  """

  def __init__(self, display_name, api, cmd_group):
    self.display_name = display_name
    self.api = api
    self.cmd_group = cmd_group


_INFO = {
    'appdevexperience':
        Info(
            display_name='CloudRun',
            api='appdevelopmentexperience.googleapis.com',
            cmd_group='cloudrun',
        ),
    'cloudbuild':
        Info(
            display_name='Cloud Build',
            api='cloudbuild.googleapis.com',
            cmd_group='build',
        ),
    'configmanagement':
        Info(
            display_name='Config Management',
            api='anthosconfigmanagement.googleapis.com',
            cmd_group='config-management',
        ),
    'identityservice':
        Info(
            display_name='Identity Service',
            api='anthosidentityservice.googleapis.com',
            cmd_group='identity-service',
        ),
    'multiclusteringress':
        Info(
            display_name='Ingress',
            api='multiclusteringress.googleapis.com',
            cmd_group='ingress',
        ),
    'multiclusterservicediscovery':
        Info(
            display_name='Multi Cluster Services',
            api='multiclusterservicediscovery.googleapis.com',
            cmd_group='multi-cluster-services',
        ),
    'servicedirectory':
        Info(
            display_name='Service Directory',
            api='servicedirectory.googleapis.com',
            cmd_group='service-directory',
        ),
    'servicemesh':
        Info(
            display_name='Service Mesh',
            api='meshconfig.googleapis.com',
            cmd_group='mesh',
        ),
}


def Get(name):
  """Get returns information about a Feature."""
  return _INFO[name]