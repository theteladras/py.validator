import unittest

from pyvalidator.is_ip import is_ip
from . import print_test_ok


class TestIsIp(unittest.TestCase):

    def test_valid_ip(self):
        for i in [
            '127.0.0.1',
            '0.0.0.0',
            '255.255.255.255',
            '1.2.3.4',
            '::1',
            '2001:db8:0000:1:1:1:1:1',
            '2001:db8:3:4::192.0.2.33',
            '2001:41d0:2:a141::1',
            '::ffff:127.0.0.1',
            '::0000',
            '0000::',
            '1::',
            '1111:1:1:1:1:1:1:1',
            'fe80::a6db:30ff:fe98:e946',
            '::',
            '::8',
            '::ffff:127.0.0.1',
            '::ffff:255.255.255.255',
            '::ffff:0:255.255.255.255',
            '::2:3:4:5:6:7:8',
            '::255.255.255.255',
            '0:0:0:0:0:ffff:127.0.0.1',
            '1:2:3:4:5:6:7::',
            '1:2:3:4:5:6::8',
            '1::7:8',
            '1:2:3:4:5::7:8',
            '1:2:3:4:5::8',
            '1::6:7:8',
            '1:2:3:4::6:7:8',
            '1:2:3:4::8',
            '1::5:6:7:8',
            '1:2:3::5:6:7:8',
            '1:2:3::8',
            '1::4:5:6:7:8',
            '1:2::4:5:6:7:8',
            '1:2::8',
            '1::3:4:5:6:7:8',
            '1::8',
            'fe80::7:8%eth0',
            'fe80::7:8%1',
            '64:ff9b::192.0.2.33',
            '0:0:0:0:0:0:10.0.0.1',
        ]:
            self.assertTrue(is_ip(i))
        print_test_ok()

    def test_invalid_ip(self):
        for i in [
            'abc',
            '256.0.0.0',
            '0.0.0.256',
            '26.0.0.256',
            '0200.200.200.200',
            '200.0200.200.200',
            '200.200.0200.200',
            '200.200.200.0200',
            '::banana',
            'banana::',
            '::1banana',
            '::1::',
            '1:',
            ':1',
            ':1:1:1::2',
            '1:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1',
            '::11111',
            '11111:1:1:1:1:1:1:1',
            '2001:db8:0000:1:1:1:1::1',
            '0:0:0:0:0:0:ffff:127.0.0.1',
            '0:0:0:0:ffff:127.0.0.1',
        ]:
            self.assertFalse(is_ip(i))
        print_test_ok()

    def test_valid_ip_v4_num(self):
        for i in [
            ['127.0.0.1', 4],
            ['0.0.0.0', 4],
            ['255.255.255.255', 4],
            ['1.2.3.4', 4],
            ['255.0.0.1', 4],
            ['0.0.1.1', 4],
        ]:
            self.assertTrue(is_ip(*i))
        print_test_ok()

    def test_invalid_ip_v4_num(self):
        for i in [
            ['::1', 4],
            ['2001:db8:0000:1:1:1:1:1', 4],
            ['::ffff:127.0.0.1', 4],
            ['137.132.10.01', 4],
            ['0.256.0.256', 4],
            ['255.256.255.256', 4],
        ]:
            self.assertFalse(is_ip(*i))
        print_test_ok()

    def test_valid_ip_v4_str(self):
        for i in [
            ['127.0.0.1', "4"],
            ['0.0.0.0', "4"],
            ['255.255.255.255', "4"],
            ['1.2.3.4', "4"],
            ['255.0.0.1', "4"],
            ['0.0.1.1', "4"],
        ]:
            self.assertTrue(is_ip(*i))
        print_test_ok()

    def test_invalid_ip_v4_str(self):
        for i in []:
            self.assertTrue(is_ip(i))
        self.assertFalse(is_ip('::1', "4"))
        self.assertFalse(is_ip('2001:db8:0000:1:1:1:1:1', "4"))
        self.assertFalse(is_ip('::ffff:127.0.0.1', "4"))
        self.assertFalse(is_ip('137.132.10.01', "4"))
        self.assertFalse(is_ip('0.256.0.256', "4"))
        self.assertFalse(is_ip('255.256.255.256', "4"))
        print_test_ok()

    def test_valid_ip_v6_num(self):
        for i in [
            ['::1', 6],
            ['2001:db8:0000:1:1:1:1:1', 6],
            ['::ffff:127.0.0.1', 6],
            ['fe80::1234%1', 6],
            ['ff08::9abc%10', 6],
            ['ff08::9abc%interface10', 6],
            ['ff02::5678%pvc1.3', 6],
        ]:
            self.assertTrue(is_ip(*i))
        print_test_ok()

    def test_invalid_ip_v6_num(self):
        for i in [
            ['127.0.0.1', 6],
            ['0.0.0.0', 6],
            ['255.255.255.255', 6],
            ['1.2.3.4', 6],
            ['::ffff:287.0.0.1', 6],
            ['%', 6],
            ['fe80::1234%', 6],
            ['fe80::1234%1%3%4', 6],
            ['fe80%fe80%', 6],
        ]:
            self.assertFalse(is_ip(*i))
        print_test_ok()

    def test_valid_ip_v6_str(self):
        for i in [
            ['::1', "6"],
            ['2001:db8:0000:1:1:1:1:1', "6"],
            ['::ffff:127.0.0.1', "6"],
            ['fe80::1234%1', "6"],
            ['ff08::9abc%10', "6"],
            ['ff08::9abc%interface10', "6"],
            ['ff02::5678%pvc1.3', "6"],
        ]:
            self.assertTrue(is_ip(*i))
        print_test_ok()

    def test_invalid_ip_v6_str(self):
        for i in [
            ['127.0.0.1', "6"],
            ['0.0.0.0', "6"],
            ['255.255.255.255', "6"],
            ['1.2.3.4', "6"],
            ['::ffff:287.0.0.1', "6"],
            ['%', "6"],
            ['fe80::1234%', "6"],
            ['fe80::1234%1%3%4', "6"],
            ['fe80%fe80%', "6"],
        ]:
            self.assertFalse(is_ip(*i))
        print_test_ok()
