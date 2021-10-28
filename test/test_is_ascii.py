import unittest
import validator

class TestIsAscii(unittest.TestCase):

    def test_valid_ascii_strings(self):
        self.assertTrue(validator.is_ascii('foobar'))
        self.assertTrue(validator.is_ascii('0987654321'))
        self.assertTrue(validator.is_ascii('test@example.com'))
        self.assertTrue(validator.is_ascii('1234abcDEF'))
        print('OK - valid_ascii_strings')

    def test_invalid_ascii_strings(self):
        self.assertFalse(validator.is_ascii('ｆｏｏbar'))
        self.assertFalse(validator.is_ascii('ｘｙｚ０９８'))
        self.assertFalse(validator.is_ascii('１２３456'))
        self.assertFalse(validator.is_ascii('ｶﾀｶﾅ'))
        print('OK - invalid_ascii_strings')
