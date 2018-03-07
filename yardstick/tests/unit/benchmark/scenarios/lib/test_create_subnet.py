##############################################################################
# Copyright (c) 2017 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import unittest
import mock

from yardstick.benchmark.scenarios.lib.create_subnet import CreateSubnet


class CreateSubnetTestCase(unittest.TestCase):

    @mock.patch('yardstick.common.openstack_utils.get_neutron_client')
    @mock.patch('yardstick.common.openstack_utils.create_neutron_subnet')
    def test_create_subnet(self, mock_get_neutron_client, mock_create_neutron_subnet):
        options = {
            'openstack_paras': {
                'network_id': '123-123-123',
                'name': 'yardstick_subnet',
                'cidr': '10.10.10.0/24',
                'ip_version': '4'
            }
        }
        args = {"options": options}
        obj = CreateSubnet(args, {})
        obj.run({})
        self.assertTrue(mock_get_neutron_client.called)
        self.assertTrue(mock_create_neutron_subnet.called)