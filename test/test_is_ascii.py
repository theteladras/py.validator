import unittest
from validator import *

class TestIsAscii(unittest.TestCase):

    def test_valid_ascii_strings(self):
        self.assertTrue(is_ascii('foobar'))
        self.assertTrue(is_ascii('0987654321'))
        self.assertTrue(is_ascii('test@example.com'))
        self.assertTrue(is_ascii('1234abcDEF'))
        print('OK - valid_ascii_strings')

    def test_invalid_ascii_strings(self):
        self.assertFalse(is_ascii('ｆｏｏbar'))
        self.assertFalse(is_ascii('ｘｙｚ０９８'))
        self.assertFalse(is_ascii('１２３456'))
        self.assertFalse(is_ascii('ｶﾀｶﾅ'))
        print('OK - invalid_ascii_strings')
