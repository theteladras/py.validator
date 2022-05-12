import unittest

from pyvalidator.is_base32 import is_base32
from . import print_test_ok


class TestIsBase32(unittest.TestCase):

    def test_valid_base32(self):
        for i in [
            'ZG======',
            'JBSQ====',
            'JBSWY===',
            'K5SWYY3PNVSSA5DPEBXG6ZA=',
            'K5SWYY3PNVSSA5DPEBXG6===',
        ]:
            self.assertTrue(is_base32(i))
        print_test_ok()

    def test_invalid_base32(self):
        for i in [
            '12345',
            '',
            'ZG=====',
            'Zm=8JBSWY3DP',
            '=m9vYg==',
            'Zm9vYm/y====',
        ]:
            self.assertFalse(is_base32(i))
        print_test_ok()
