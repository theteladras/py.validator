import unittest
from pyvalidator import *

class TestIsUppercase(unittest.TestCase):

    def test_valid_uppercase(self):
        self.assertTrue(is_uppercase('CCC'))
        self.assertTrue(is_uppercase('UYTREWQ'))
        self.assertTrue(is_uppercase('ASD123'))
        self.assertTrue(is_uppercase('HELLO WORLD'))
        self.assertTrue(is_uppercase('   .'))
        print('OK - test_valid_uppercase')

    def test_invalid_uppercase(self):
        self.assertFalse(is_uppercase('hello world'))
        self.assertFalse(is_uppercase('HELLO WORLd'))
        self.assertFalse(is_uppercase('asd123'))
        print('OK - test_invalid_uppercase')
