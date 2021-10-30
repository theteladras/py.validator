import unittest
import validator

class TestIsNumber(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertTrue(validator.is_number('13'))
        self.assertTrue(validator.is_number('123'))
        self.assertTrue(validator.is_number('0.11'))
        self.assertTrue(validator.is_number('-0'))
        self.assertTrue(validator.is_number('+1.1'))
        self.assertTrue(validator.is_number('012'))
        self.assertTrue(validator.is_number('-013'))
        self.assertTrue(validator.is_number('000'))
        self.assertTrue(validator.is_number('123.123'))
        self.assertTrue(validator.is_number('-123٫123'))
        self.assertTrue(validator.is_number('+0٫123'))
        self.assertTrue(validator.is_number('-0.11250738585072011e-307'))
        print('OK - test_valid_numbers')

    def test_invalid_numbers(self):
        self.assertFalse(validator.is_number('123,123,asd'))
        self.assertFalse(validator.is_number('asd'))
        self.assertFalse(validator.is_number('.'))
        self.assertFalse(validator.is_number('   '))
        self.assertFalse(validator.is_number(''))
        self.assertFalse(validator.is_number(','))
        self.assertFalse(validator.is_number('foofoo'))
        self.assertFalse(validator.is_number('2^3'))
        self.assertFalse(validator.is_number('2+3'))
        print('OK - test_invalid_numbers')
