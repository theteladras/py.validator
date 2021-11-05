import unittest
from validator import *

class TestIsHexadecimal(unittest.TestCase):

    def test_valid_hexadecimal(self):
        self.assertTrue(is_hexadecimal('AA'))
        self.assertTrue(is_hexadecimal('deadBEEF'))
        self.assertTrue(is_hexadecimal('ff0044'))
        self.assertTrue(is_hexadecimal('0xff0044'))
        self.assertTrue(is_hexadecimal('0XfF0044'))
        self.assertTrue(is_hexadecimal('0x0123456789abcDEF'))
        self.assertTrue(is_hexadecimal('0X0123456789abcDEF'))
        self.assertTrue(is_hexadecimal('0hfedCBA9876543210'))
        self.assertTrue(is_hexadecimal('0HfedCBA9876543210'))
        self.assertTrue(is_hexadecimal('0123456789abcDEF'))
        print('OK - test_valid_hexadecimal')

    def test_invalid_hexadecimal(self):
        self.assertFalse(is_hexadecimal(''))
        self.assertFalse(is_hexadecimal('.'))
        self.assertFalse(is_hexadecimal('..'))
        self.assertFalse(is_hexadecimal('AA/'))
        self.assertFalse(is_hexadecimal('A A'))
        self.assertFalse(is_hexadecimal('abcdefg'))
        self.assertFalse(is_hexadecimal('0xa2h'))
        self.assertFalse(is_hexadecimal('0xa20x'))
        self.assertFalse(is_hexadecimal('0x0123456789abcDEFq'))
        self.assertFalse(is_hexadecimal('0hfedCBA9876543210q'))
        self.assertFalse(is_hexadecimal('01234q56789abcDEF'))
        print('OK - test_invalid_hexadecimal')
