import unittest
from validator import *

class TestIsBase32(unittest.TestCase):

    def test_valid_base32(self):
        self.assertTrue(is_base32('ZG======'))
        self.assertTrue(is_base32('JBSQ===='))
        self.assertTrue(is_base32('JBSWY==='))
        self.assertTrue(is_base32('K5SWYY3PNVSSA5DPEBXG6ZA='))
        self.assertTrue(is_base32('K5SWYY3PNVSSA5DPEBXG6==='))
        print('OK - test_valid_base32')

    def test_invalid_base32(self):
        self.assertFalse(is_base32('12345'))
        self.assertFalse(is_base32(''))
        self.assertFalse(is_base32('ZG====='))
        self.assertFalse(is_base32('Zm=8JBSWY3DP'))
        self.assertFalse(is_base32('=m9vYg=='))
        self.assertFalse(is_base32('Zm9vYm/y===='))
        print('OK - test_invalid_base32')
