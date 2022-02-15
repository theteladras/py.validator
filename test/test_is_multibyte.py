import unittest
from pyvalidator import *

class TestIsMultiByte(unittest.TestCase):

    def test_valid_multibyte(self):
        self.assertTrue(is_multibyte('ひらがな・カタカナ、．漢字'))
        self.assertTrue(is_multibyte('あいうえお foobar'))
        self.assertTrue(is_multibyte('ｶﾀｶﾅ'))
        self.assertTrue(is_multibyte('中文'))
        self.assertTrue(is_multibyte('test＠example.com'))
        self.assertTrue(is_multibyte('1234abcDEｘｙｚ'))
        print('OK - test_valid_multibyte')

    def test_invalid_multibyte(self):
        self.assertFalse(is_multibyte('abc'))
        self.assertFalse(is_multibyte('abc123'))
        self.assertFalse(is_multibyte('<>@" *.'))
        print('OK - test_invalid_multibyte')
