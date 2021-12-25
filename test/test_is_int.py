import unittest
from pyvalidator import *

class TestIsInt(unittest.TestCase):

    def test_valid_ints(self):
        self.assertTrue(is_int('13'))
        self.assertTrue(is_int('123'))
        self.assertTrue(is_int('0'))
        self.assertTrue(is_int('-0'))
        self.assertTrue(is_int('+1'))
        self.assertTrue(is_int('01'))
        self.assertTrue(is_int('-01'))
        self.assertTrue(is_int('000'))
        print('OK - test_valid_ints')

    def test_invalid_ints(self):
        self.assertFalse(is_int('100e10'))
        self.assertFalse(is_int('123.123'))
        self.assertFalse(is_int('   '))
        self.assertFalse(is_int(''))
        self.assertFalse(is_int('.'))
        self.assertFalse(is_int('foo'))
        print('OK - test_invalid_ints')

    def test_valid_ints_dont_allow_leading_zeroes(self) -> bool:
        self.assertTrue(is_int('13', { "allow_leading_zeroes": False }))
        self.assertTrue(is_int('11', { "allow_leading_zeroes": False }))
        self.assertTrue(is_int('123', { "allow_leading_zeroes": False }))
        self.assertTrue(is_int('0', { "allow_leading_zeroes": False }))
        self.assertTrue(is_int('-0', { "allow_leading_zeroes": False }))
        self.assertTrue(is_int('+1', { "allow_leading_zeroes": False }))
        print('OK - test_valid_ints_dont_allow_leading_zeroes')

    def test_invalid_ints_dont_allow_leading_zeroes(self):
        self.assertFalse(is_int('01', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('-01', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('000', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('100e10', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('123.11', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('foo', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('   ', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('\n', { "allow_leading_zeroes": False }))
        self.assertFalse(is_int('\t', { "allow_leading_zeroes": False }))
        print('OK - test_invalid_ints_dont_allow_leading_zeroes')

    def test_fail_ints(self):
        self.assertRaises(Exception, is_int, None)
        self.assertRaises(Exception, is_int, {})
