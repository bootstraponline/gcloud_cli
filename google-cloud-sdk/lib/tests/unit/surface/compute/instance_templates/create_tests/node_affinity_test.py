# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base as calliope_base
from googlecloudsdk.command_lib.compute.sole_tenancy import util as sole_tenancy_util
from tests.lib import parameterized
from tests.lib import test_case
from tests.lib.surface.compute.instance_templates import create_test_base


class InstanceTemplatesCreateWithNodeAffinity(
    create_test_base.InstanceTemplatesCreateTestBase, parameterized.TestCase):
  """Test creation of VM instances on sole tenant host."""

  def PreSetUp(self):
    self.track = calliope_base.ReleaseTrack.GA
    self.api_version = 'v1'

  def SetUp(self):
    self.node_affinity = self.messages.SchedulingNodeAffinity
    self.operator_enum = self.node_affinity.OperatorValueValuesEnum

  def _CheckCreateRequests(self, node_affinities):
    m = self.messages
    prop = m.InstanceProperties(
        canIpForward=False,
        disks=[
            m.AttachedDisk(
                autoDelete=True,
                boot=True,
                initializeParams=m.AttachedDiskInitializeParams(
                    sourceImage=self._default_image,),
                mode=m.AttachedDisk.ModeValueValuesEnum.READ_WRITE,
                type=m.AttachedDisk.TypeValueValuesEnum.PERSISTENT)
        ],
        machineType=create_test_base.DEFAULT_MACHINE_TYPE,
        metadata=m.Metadata(),
        networkInterfaces=[
            m.NetworkInterface(
                accessConfigs=[self._default_access_config],
                network=self._default_network)
        ],
        serviceAccounts=[
            m.ServiceAccount(
                email='default', scopes=create_test_base.DEFAULT_SCOPES),
        ],
        scheduling=m.Scheduling(
            automaticRestart=True, nodeAffinities=node_affinities),
    )
    template = m.InstanceTemplate(name='template-1', properties=prop)

    self.CheckRequests(
        self.get_default_image_requests,
        [(self.compute.instanceTemplates, 'Insert',
          m.ComputeInstanceTemplatesInsertRequest(
              instanceTemplate=template,
              project='my-project',
          ))],
    )

  def testCreate_SimpleNodeAffinityJson(self):
    node_affinities = [
        self.node_affinity(
            key='key1',
            operator=self.operator_enum.IN,
            values=['value1', 'value2'])
    ]
    contents = """\
[{"operator": "IN", "values": ["value1", "value2"], "key": "key1"}]
    """
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    self.Run("""
        compute instance-templates create template-1
          --node-affinity-file {}
        """.format(node_affinity_file))

    self._CheckCreateRequests(node_affinities)

  def testCreate_SimpleNodeAffinityYaml(self):
    node_affinities = [
        self.node_affinity(
            key='key1',
            operator=self.operator_enum.IN,
            values=['value1', 'value2'])
    ]
    contents = """\
- key: key1
  operator: IN
  values: [value1, value2]
    """
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    self.Run("""
        compute instance-templates create template-1
          --node-affinity-file {}
        """.format(node_affinity_file))

    self._CheckCreateRequests(node_affinities)

  def testCreate_MultipleNodeAffinityMessages(self):
    node_affinities = [
        self.node_affinity(
            key='key1', operator=self.operator_enum.IN, values=['value1']),
        self.node_affinity(
            key='key2',
            operator=self.operator_enum.NOT_IN,
            values=['value2', 'value3']),
        self.node_affinity(
            key='key3', operator=self.operator_enum.IN, values=[])
    ]
    contents = """\
- key: key1
  operator: IN
  values: [value1]
- key: key2
  operator: NOT_IN
  values: [value2, value3]
- key: key3
  operator: IN
    """
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    self.Run("""
        compute instance-templates create template-1
          --node-affinity-file {}
        """.format(node_affinity_file))

    self._CheckCreateRequests(node_affinities)

  def testCreate_InvalidOperator(self):
    contents = """\
- key: key1
  operator: HelloWorld
  values: [value1, value2]
    """
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    with self.AssertRaisesExceptionMatches(
        sole_tenancy_util.NodeAffinityFileParseError,
        "Key [key1] has invalid field formats for: ['operator']"):
      self.Run("""
          compute instance-templates create template-1
            --node-affinity-file {}
          """.format(node_affinity_file))

  def testCreate_NoKey(self):
    contents = """\
- operator: IN
  values: [value1, value2]
    """
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    with self.AssertRaisesExceptionMatches(
        sole_tenancy_util.NodeAffinityFileParseError,
        'A key must be specified for every node affinity label.'):
      self.Run("""
          compute instance-templates create template-1
            --node-affinity-file {}
          """.format(node_affinity_file))

  def testCreate_InvalidYaml(self):
    contents = """\
- key: key1
  operator: IN
  values: 3
    """
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    with self.AssertRaisesExceptionRegexp(
        sole_tenancy_util.NodeAffinityFileParseError,
        r"Expected type <(class|type) '(str|unicode)'> for field values, found "
        r"3 \(type <(class|type) 'int'>\)"):
      self.Run("""
          compute instance-templates create template-1
            --node-affinity-file {}
          """.format(node_affinity_file))

  @parameterized.parameters('-', '[{}]')
  def testCreate_EmptyListItem(self, contents):
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    with self.AssertRaisesExceptionMatches(
        sole_tenancy_util.NodeAffinityFileParseError,
        'Empty list item in JSON/YAML file.'):
      self.Run("""
          compute instance-templates create template-1
            --node-affinity-file {}
          """.format(node_affinity_file))

  @parameterized.parameters('', '[]')
  def testCreate_AffinityFileWithLabels(self, contents):
    node_affinity_file = self.Touch(
        self.temp_path, 'affinity_config.json', contents=contents)
    with self.AssertRaisesExceptionMatches(
        sole_tenancy_util.NodeAffinityFileParseError,
        'No node affinity labels specified. You must specify at least one '
        'label to create a sole tenancy instance.'):
      self.Run("""
          compute instance-templates create template-1
            --node-affinity-file {}
          """.format(node_affinity_file))

  def testCreate_NodeGroup(self):
    node_affinities = [
        self.node_affinity(
            key='compute.googleapis.com/node-group-name',
            operator=self.operator_enum.IN,
            values=['my-node-group'])
    ]
    self.Run("""
        compute instance-templates create template-1
          --node-group my-node-group
        """)

    self._CheckCreateRequests(node_affinities)

  def testCreate_Node(self):
    node_affinities = [
        self.node_affinity(
            key='compute.googleapis.com/node-name',
            operator=self.operator_enum.IN,
            values=['my-node'])
    ]
    self.Run("""
        compute instance-templates create template-1
          --node my-node
        """)

    self._CheckCreateRequests(node_affinities)


if __name__ == '__main__':
  test_case.main()