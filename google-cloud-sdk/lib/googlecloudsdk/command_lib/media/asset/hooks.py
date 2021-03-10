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
"""Create hooks for Cloud Media Asset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.core import properties

PARENT_TEMPLATE = 'projects/{}/locations/{}'


def AddDefaultParentInfoToAssetTypeRequests(ref, args, req):
  """Python hook for yaml commands to wildcard the location in asset type requests."""
  del ref  # Unused
  project = properties.VALUES.core.project.Get(required=True)
  location = args.location or properties.VALUES.media_asset.location.Get(
      required=True)
  req.parent = PARENT_TEMPLATE.format(project, location)
  return req
