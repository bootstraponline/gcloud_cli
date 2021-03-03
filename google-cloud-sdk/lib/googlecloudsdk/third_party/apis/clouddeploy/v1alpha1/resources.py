# -*- coding: utf-8 -*- #
# Copyright 2015 Google LLC. All Rights Reserved.
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
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://clouddeploy.googleapis.com/v1alpha1/'
DOCS_URL = ''


class Collections(enum.Enum):
  """Collections for all supported apis."""

  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      ['projectsId'],
      True
  )
  PROJECTS_DELIVERYPIPELINES = (
      'projects.deliveryPipelines',
      'projects/{projectsId}/deliveryPipelines/{deliveryPipelinesId}',
      {},
      ['projectsId', 'deliveryPipelinesId'],
      True
  )
  PROJECTS_DELIVERYPIPELINES_RELEASES = (
      'projects.deliveryPipelines.releases',
      'projects/{projectsId}/deliveryPipelines/{deliveryPipelinesId}/'
      'releases/{releasesId}',
      {},
      ['projectsId', 'deliveryPipelinesId', 'releasesId'],
      True
  )
  PROJECTS_DELIVERYPIPELINES_RELEASES_DELIVERYPIPELINES = (
      'projects.deliveryPipelines.releases.deliveryPipelines',
      '{+name}',
      {
          '':
              'projects/{projectsId}/deliveryPipelines/{deliveryPipelinesId}/'
              'releases/{releasesId}/deliveryPipelines/{deliveryPipelinesId1}',
      },
      ['name'],
      True
  )
  PROJECTS_DELIVERYPIPELINES_RELEASES_TARGETS = (
      'projects.deliveryPipelines.releases.targets',
      '{+name}',
      {
          '':
              'projects/{projectsId}/deliveryPipelines/{deliveryPipelinesId}/'
              'releases/{releasesId}/targets/{targetsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS = (
      'projects.locations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_DELIVERYPIPELINES = (
      'projects.locations.deliveryPipelines',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'deliveryPipelines/{deliveryPipelinesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_DELIVERYPIPELINES_RELEASES = (
      'projects.locations.deliveryPipelines.releases',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'deliveryPipelines/{deliveryPipelinesId}/releases/{releasesId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_DELIVERYPIPELINES_RELEASES_ROLLOUTS = (
      'projects.locations.deliveryPipelines.releases.rollouts',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'deliveryPipelines/{deliveryPipelinesId}/releases/{releasesId}/'
              'rollouts/{rolloutsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_DELIVERYPIPELINES_TARGETS = (
      'projects.locations.deliveryPipelines.targets',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/'
              'deliveryPipelines/{deliveryPipelinesId}/targets/{targetsId}',
      },
      ['name'],
      True
  )
  PROJECTS_LOCATIONS_OPERATIONS = (
      'projects.locations.operations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/operations/'
              '{operationsId}',
      },
      ['name'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing
