import unittest
from pyvalidator import *

class TestIsNumber(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertTrue(is_number('13'))
        self.assertTrue(is_number('123'))
        self.assertTrue(is_number('0.11'))
        self.assertTrue(is_number('-0'))
        self.assertTrue(is_number('+1.1'))
        self.assertTrue(is_number('012'))
        self.assertTrue(is_number('-013'))
        self.assertTrue(is_number('000'))
        self.assertTrue(is_number('123.123'))
        self.assertTrue(is_number('-123٫123'))
        self.assertTrue(is_number('+0٫123'))
        self.assertTrue(is_number('-0.11250738585072011e-307'))
        print('OK - test_valid_numbers')

    def test_invalid_numbers(self):
        self.assertFalse(is_number('123,123,asd'))
        self.assertFalse(is_number('asd'))
        self.assertFalse(is_number('.'))
        self.assertFalse(is_number('   '))
        self.assertFalse(is_number(''))
        self.assertFalse(is_number(','))
        self.assertFalse(is_number('foofoo'))
        self.assertFalse(is_number('2^3'))
        self.assertFalse(is_number('2+3'))
        print('OK - test_invalid_numbers')
