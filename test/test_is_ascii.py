import unittest

from pyvalidator.is_ascii import is_ascii
from . import print_test_ok


class TestIsAscii(unittest.TestCase):

    def test_valid_ascii_strings(self):
        for i in [
            'foobar',
            '0987654321',
            'test@example.com',
            '1234abcDEF',
        ]:
            self.assertTrue(is_ascii(i))
        print_test_ok()

    def test_invalid_ascii_strings(self):
        for i in [
            'ｆｏｏbar',
            'ｘｙｚ０９８',
            '１２３456',
            'ｶﾀｶﾅ',
        ]:
            self.assertFalse(is_ascii(i))
        print_test_ok()
