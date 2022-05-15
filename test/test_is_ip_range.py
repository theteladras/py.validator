import unittest

from pyvalidator.is_ip_range import is_ip_range
from . import print_test_ok


class TestIsIpRange(unittest.TestCase):

    def test_valid_ip_range(self):
        for i in [
            '127.0.0.1/24',
            '0.0.0.0/0',
            '255.255.255.0/32',
            '::/0',
            '::/128',
            '2001::/128',
            '2001:800::/128',
            '::ffff:127.0.0.1/128',
        ]:
            self.assertTrue(is_ip_range(i))
        print_test_ok()

    def test_invalid_ip_range(self):
        for i in [
            'abc',
            '127.200.230.1/35',
            '127.200.230.1/-1',
            '1.1.1.1/011',
            '1.1.1/24.1',
            '1.1.1.1/01',
            '1.1.1.1/1.1',
            '1.1.1.1/1.',
            '1.1.1.1/1/1',
            '1.1.1.1',
            '::1',
            '::1/164',
            '2001::/240',
            '2001::/-1',
            '2001::/001',
            '2001::/24.1',
            '2001:db8:0000:1:1:1:1:1',
            '::ffff:127.0.0.1',
        ]:
            self.assertFalse(is_ip_range(i))
        print_test_ok()

    def test_valid_ip_range_v4(self):
        for i in [
            ['127.0.0.1/1', 4],
            ['0.0.0.0/1', 4],
            ['255.255.255.255/1', 4],
            ['1.2.3.4/1', 4],
            ['255.0.0.1/1', 4],
            ['0.0.1.1/1', 4],
        ]:
            self.assertTrue(is_ip_range(*i))
        print_test_ok()

    def test_invalid_ip_range_v4(self):
        for i in [
            ['abc', 4],
            ['::1', 4],
            ['2001:db8:0000:1:1:1:1:1', 4],
            ['::ffff:127.0.0.1', 4],
            ['137.132.10.01', 4],
            ['0.256.0.256', 4],
            ['255.256.255.256', 4],
        ]:
            self.assertFalse(is_ip_range(*i))
        print_test_ok()

    def test_valid_ip_range_v6(self):
        for i in [
            ['::1/1', 6],
            ['2001:db8:0000:1:1:1:1:1/1', 6],
            ['::ffff:127.0.0.1/1', 6],
        ]:
            self.assertTrue(is_ip_range(*i))
        print_test_ok()

    def test_invalid_ip_range_v6(self):
        for i in [
            ['abc', 6],
            ['127.0.0.1', 6],
            ['0.0.0.0', 6],
            ['255.255.255.255', 6],
            ['1.2.3.4', 6],
            ['::ffff:287.0.0.1', 6],
            ['::ffff:287.0.0.1/254', 6],
            ['%', 6],
            ['fe80::1234%', 6],
            ['fe80::1234%1%3%4', 6],
            ['fe80%fe80%', 6],
        ]:
            self.assertFalse(is_ip_range(*i))
        print_test_ok()

    def test_invalid_ip_range_v10(self):
        for i in [
            ['abc', 10],
            ['127.0.0.1/1', 10],
            ['0.0.0.0/1', 10],
            ['255.255.255.255/1', 10],
        ]:
            self.assertFalse(is_ip_range(*i))
        print_test_ok()
