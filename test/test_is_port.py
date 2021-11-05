import unittest
from validator import *

class TestIsPort(unittest.TestCase):

    def test_valid_port(self):
        self.assertTrue(is_port('0'))
        self.assertTrue(is_port('22'))
        self.assertTrue(is_port('80'))
        self.assertTrue(is_port('443'))
        self.assertTrue(is_port('5000'))
        self.assertTrue(is_port('8000'))
        self.assertTrue(is_port('65535'))
        print('OK - test_valid_port')

    def test_invalid_port(self):
        self.assertFalse(is_port(''))
        self.assertFalse(is_port('-1'))
        self.assertFalse(is_port('65536'))
        self.assertFalse(is_port('655369'))
        self.assertFalse(is_port('.'))
        print('OK - test_invalid_port')
