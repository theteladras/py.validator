import unittest
from pyvalidator import *

class TestIsIpRange(unittest.TestCase):

    def test_valid_ip_range(self):
        self.assertTrue(is_ip_range('127.0.0.1/24'))
        self.assertTrue(is_ip_range('0.0.0.0/0'))
        self.assertTrue(is_ip_range('255.255.255.0/32'))
        self.assertTrue(is_ip_range('::/0'))
        self.assertTrue(is_ip_range('::/128'))
        self.assertTrue(is_ip_range('2001::/128'))
        self.assertTrue(is_ip_range('2001:800::/128'))
        self.assertTrue(is_ip_range('::ffff:127.0.0.1/128'))
        print('OK - test_valid_ip_range')

    def test_invalid_ip_range(self):
        self.assertFalse(is_ip_range('abc'))
        self.assertFalse(is_ip_range('127.200.230.1/35'))
        self.assertFalse(is_ip_range('127.200.230.1/-1'))
        self.assertFalse(is_ip_range('1.1.1.1/011'))
        self.assertFalse(is_ip_range('1.1.1/24.1'))
        self.assertFalse(is_ip_range('1.1.1.1/01'))
        self.assertFalse(is_ip_range('1.1.1.1/1.1'))
        self.assertFalse(is_ip_range('1.1.1.1/1.'))
        self.assertFalse(is_ip_range('1.1.1.1/1/1'))
        self.assertFalse(is_ip_range('1.1.1.1'))
        self.assertFalse(is_ip_range('::1'))
        self.assertFalse(is_ip_range('::1/164'))
        self.assertFalse(is_ip_range('2001::/240'))
        self.assertFalse(is_ip_range('2001::/-1'))
        self.assertFalse(is_ip_range('2001::/001'))
        self.assertFalse(is_ip_range('2001::/24.1'))
        self.assertFalse(is_ip_range('2001:db8:0000:1:1:1:1:1'))
        self.assertFalse(is_ip_range('::ffff:127.0.0.1'))
        print('OK - test_invalid_ip_range')

    def test_valid_ip_range_v4(self):
        self.assertTrue(is_ip_range('127.0.0.1/1', 4))
        self.assertTrue(is_ip_range('0.0.0.0/1', 4))
        self.assertTrue(is_ip_range('255.255.255.255/1', 4))
        self.assertTrue(is_ip_range('1.2.3.4/1', 4))
        self.assertTrue(is_ip_range('255.0.0.1/1', 4))
        self.assertTrue(is_ip_range('0.0.1.1/1', 4))
        print('OK - test_valid_ip_range_v4')

    def test_invalid_ip_range_v4(self):
        self.assertFalse(is_ip_range('abc', 4))
        self.assertFalse(is_ip_range('::1', 4))
        self.assertFalse(is_ip_range('2001:db8:0000:1:1:1:1:1', 4))
        self.assertFalse(is_ip_range('::ffff:127.0.0.1', 4))
        self.assertFalse(is_ip_range('137.132.10.01', 4))
        self.assertFalse(is_ip_range('0.256.0.256', 4))
        self.assertFalse(is_ip_range('255.256.255.256', 4))
        print('OK - test_invalid_ip_range_v4')

    def test_valid_ip_range_v6(self):
        self.assertTrue(is_ip_range('::1/1', 6))
        self.assertTrue(is_ip_range('2001:db8:0000:1:1:1:1:1/1', 6))
        self.assertTrue(is_ip_range('::ffff:127.0.0.1/1', 6))
        print('OK - test_valid_ip_range_v6')

    def test_invalid_ip_range_v6(self):
        self.assertFalse(is_ip_range('abc', 6))
        self.assertFalse(is_ip_range('127.0.0.1', 6))
        self.assertFalse(is_ip_range('0.0.0.0', 6))
        self.assertFalse(is_ip_range('255.255.255.255', 6))
        self.assertFalse(is_ip_range('1.2.3.4', 6))
        self.assertFalse(is_ip_range('::ffff:287.0.0.1', 6))
        self.assertFalse(is_ip_range('::ffff:287.0.0.1/254', 6))
        self.assertFalse(is_ip_range('%', 6))
        self.assertFalse(is_ip_range('fe80::1234%', 6))
        self.assertFalse(is_ip_range('fe80::1234%1%3%4', 6))
        self.assertFalse(is_ip_range('fe80%fe80%', 6))
        print('OK - test_invalid_ip_range_v6')

    def test_invalid_ip_range_v10(self):
        self.assertFalse(is_ip_range('abc', 10))
        self.assertFalse(is_ip_range('127.0.0.1/1', 10))
        self.assertFalse(is_ip_range('0.0.0.0/1', 10))
        self.assertFalse(is_ip_range('255.255.255.255/1', 10))
        print('OK - test_invalid_ip_range_v6')
