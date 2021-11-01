import unittest
import validator

class TestIsUppercase(unittest.TestCase):

    def test_valid_uppercase(self):
        self.assertTrue(validator.is_uppercase('CCC'))
        self.assertTrue(validator.is_uppercase('UYTREWQ'))
        self.assertTrue(validator.is_uppercase('ASD123'))
        self.assertTrue(validator.is_uppercase('HELLO WORLD'))
        self.assertTrue(validator.is_uppercase('   .'))
        print('OK - test_valid_uppercase')

    def test_invalid_uppercase(self):
        self.assertFalse(validator.is_uppercase('hello world'))
        self.assertFalse(validator.is_uppercase('HELLO WORLd'))
        self.assertFalse(validator.is_uppercase('asd123'))
        print('OK - test_invalid_uppercase')
