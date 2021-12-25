import unittest
from pyvalidator import *

class TestIsLowercase(unittest.TestCase):

    def test_valid_lowercase(self):
        self.assertTrue(is_lowercase('ccc'))
        self.assertTrue(is_lowercase('qwerty'))
        self.assertTrue(is_lowercase('asd123'))
        self.assertTrue(is_lowercase('hello world'))
        self.assertTrue(is_lowercase('   .'))
        print('OK - test_valid_lowercase')

    def test_invalid_lowercase(self):
        self.assertFalse(is_lowercase('hello WoRLD'))
        self.assertFalse(is_lowercase('HELLO WORLd'))
        self.assertFalse(is_lowercase('ASD123'))
        print('OK - test_invalid_lowercase')
