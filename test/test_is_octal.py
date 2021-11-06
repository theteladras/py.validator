import unittest
from validator import *

class TestIsOctal(unittest.TestCase):

    def test_valid_octal(self):
        self.assertTrue(is_octal('076543210'))
        self.assertTrue(is_octal('0o01234567'))
        print('OK - test_valid_octal')

    def test_invalid_octal(self):
        self.assertFalse(is_octal(''))
        self.assertFalse(is_octal('.'))
        self.assertFalse(is_octal('/'))
        self.assertFalse(is_octal('999'))
        self.assertFalse(is_octal('abcdefg'))
        self.assertFalse(is_octal('012345678'))
        self.assertFalse(is_octal('012345670c'))
        self.assertFalse(is_octal('00c12345670c'))
        print('OK - test_invalid_octal')
