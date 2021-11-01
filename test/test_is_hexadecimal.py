import unittest
import validator

class TestIsHexadecimal(unittest.TestCase):

    def test_valid_hexadecimal(self):
        self.assertTrue(validator.is_hexadecimal('AA'))
        self.assertTrue(validator.is_hexadecimal('deadBEEF'))
        self.assertTrue(validator.is_hexadecimal('ff0044'))
        self.assertTrue(validator.is_hexadecimal('0xff0044'))
        self.assertTrue(validator.is_hexadecimal('0XfF0044'))
        self.assertTrue(validator.is_hexadecimal('0x0123456789abcDEF'))
        self.assertTrue(validator.is_hexadecimal('0X0123456789abcDEF'))
        self.assertTrue(validator.is_hexadecimal('0hfedCBA9876543210'))
        self.assertTrue(validator.is_hexadecimal('0HfedCBA9876543210'))
        self.assertTrue(validator.is_hexadecimal('0123456789abcDEF'))
        print('OK - test_valid_hexadecimal')

    def test_invalid_hexadecimal(self):
        self.assertFalse(validator.is_hexadecimal(''))
        self.assertFalse(validator.is_hexadecimal('.'))
        self.assertFalse(validator.is_hexadecimal('..'))
        self.assertFalse(validator.is_hexadecimal('AA/'))
        self.assertFalse(validator.is_hexadecimal('A A'))
        self.assertFalse(validator.is_hexadecimal('abcdefg'))
        self.assertFalse(validator.is_hexadecimal('0xa2h'))
        self.assertFalse(validator.is_hexadecimal('0xa20x'))
        self.assertFalse(validator.is_hexadecimal('0x0123456789abcDEFq'))
        self.assertFalse(validator.is_hexadecimal('0hfedCBA9876543210q'))
        self.assertFalse(validator.is_hexadecimal('01234q56789abcDEF'))
        print('OK - test_invalid_hexadecimal')
