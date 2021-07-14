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
"""Flags and helpers for the compute future reservations commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute.instances import flags as instance_flags
from googlecloudsdk.command_lib.compute.reservations import flags as reservation_flags


def GetNamePrefixFlag():
  """Gets the --name-prefix flag."""
  help_text = """\
  User provided name prefix for system generated reservations when capacity is
  delivered at start time.
  """
  return base.Argument('--name-prefix', help=help_text)


def GetTotalCountFlag(required=True):
  """Gets the --total-count flag."""
  help_text = """\
  The total number of instances for which capacity assurance is requested at a
  future time period.
  """
  return base.Argument(
      '--total-count', required=required, type=int, help=help_text)


def GetStartTimeFlag(required=True):
  """Gets the --start-time flag."""
  return base.Argument(
      '--start-time', required=required, type=str, help=GetStartTimeHelpText())


def GetStartTimeHelpText():
  """Gets the --start-time help text."""
  help_text = """\
  Start time of the Future Reservation. The start time must be an RFC3399 valid
  string formatted by date, time, and timezone or "YYYY-MM-DDTHH:MM:SSZ"; where
  YYYY = year, MM = month, DD = day, HH = hours, MM = minutes, SS = seconds, and
  Z = timezone (i.e. 2021-11-20T07:00:00Z).
  """
  return help_text


def GetEndTimeHelpText():
  """Gets the --end-time help text."""
  help_text = """\
  End time of the Future Reservation. The end time must be an RFC3399 valid
  string formatted by date, time, and timezone or "YYYY-MM-DDTHH:MM:SSZ"; where
  YYYY = year, MM = month, DD = day, HH = hours, MM = minutes, SS = seconds, and
  Z = timezone (i.e. 2021-11-20T07:00:00Z).
  """
  return help_text


def GetDurationHelpText():
  """Gets the --duration help text."""
  help_text = """\
  Alternate way of specifying time in the number of seconds to terminate
  capacity request relative to the start time of a request.
  """
  return help_text


def GetSharedSettingFlag(custom_name=None):
  """Gets the --share-setting flag."""
  help_text = """\
  Specify if this reservation is shared; and if so, the type of sharing: share
  with specific projects.
  """
  return base.Argument(
      custom_name if custom_name else '--share-setting',
      choices=['projects'],
      help=help_text)


def GetShareWithFlag(custom_name=None):
  """Gets the --share-with flag."""
  help_text = """\
  A list of specific projects this reservation should be shared with.
  List must contain all project ID's.
  """
  return base.Argument(
      custom_name if custom_name else '--share-with',
      type=arg_parsers.ArgList(min_length=1),
      metavar='PROJECT',
      help=help_text)


def AddCreateFlags(
    parser,
    support_location_hint=False,
    support_share_setting=False,
    support_fleet=False,
):
  """Adds all flags needed for the create command."""
  GetNamePrefixFlag().AddToParser(parser)
  GetTotalCountFlag().AddToParser(parser)
  reservation_flags.GetDescriptionFlag().AddToParser(parser)

  group = base.ArgumentGroup(
      'Manage the specific SKU reservation properties.', required=True)
  group.AddArgument(reservation_flags.GetMachineType())
  group.AddArgument(reservation_flags.GetMinCpuPlatform())
  group.AddArgument(reservation_flags.GetLocalSsdFlag())
  group.AddArgument(reservation_flags.GetAcceleratorFlag())
  if support_location_hint:
    group.AddArgument(reservation_flags.GetLocationHint())
  if support_fleet:
    group.AddArgument(instance_flags.AddMaintenanceFreezeDuration())
    group.AddArgument(instance_flags.AddMaintenanceInterval())
  group.AddToParser(parser)

  time_window_group = parser.add_group(
      help='Manage the time specific properties for requesting future capacity',
      required=True)
  time_window_group.add_argument(
      '--start-time', required=True, help=GetStartTimeHelpText())
  end_time_window_group = time_window_group.add_mutually_exclusive_group(
      required=True)
  end_time_window_group.add_argument('--end-time', help=GetEndTimeHelpText())
  end_time_window_group.add_argument(
      '--duration', type=int, help=GetDurationHelpText())

  if support_share_setting:
    share_group = base.ArgumentGroup(
        'Manage the properties of a shared reservation.', required=False)
    share_group.AddArgument(GetSharedSettingFlag())
    share_group.AddArgument(GetShareWithFlag())
    share_group.AddToParser(parser)