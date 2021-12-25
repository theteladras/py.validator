import unittest
from pyvalidator import *

class TestIsByteLength(unittest.TestCase):

    def test_valid_byte_length_min_2(self):
        self.assertTrue(is_byte_length('abc', { "min": 2 }))
        self.assertTrue(is_byte_length('de', { "min": 2 }))
        self.assertTrue(is_byte_length('abcd', { "min": 2 }))
        self.assertTrue(is_byte_length('ｇｍａｉｌ', { "min": 2 }))
        print('OK - test_valid_byte_length')

    def test_invalid_byte_length_min_2(self):
        self.assertFalse(is_byte_length('', { "min": 2 }))
        self.assertFalse(is_byte_length('a', { "min": 2 }))
        print('OK - test_invalid_byte_length')

    def test_valid_byte_length_min_2_max_3(self):
        self.assertTrue(is_byte_length('abc', { "min": 2, "max": 3 }))
        self.assertTrue(is_byte_length('de', { "min": 2, "max": 3 }))
        self.assertTrue(is_byte_length('ｇ', { "min": 2, "max": 3 }))
        print('OK - test_valid_byte_length')

    def test_invalid_byte_length_min_2_max_3(self):
        self.assertFalse(is_byte_length('', { "min": 2, "max": 3 }))
        self.assertFalse(is_byte_length('a', { "min": 2, "max": 3 }))
        self.assertFalse(is_byte_length('abcd', { "min": 2, "max": 3 }))
        self.assertFalse(is_byte_length('ｇｍ', { "min": 2, "max": 3 }))
        print('OK - test_invalid_byte_length')

    def test_valid_byte_length_max_0(self):
        self.assertTrue(is_byte_length('', { "max": 0 }))
        print('OK - test_valid_byte_length')

    def test_invalid_byte_length_max_0(self):
        self.assertFalse(is_byte_length('g', { "max": 0 }))
        self.assertFalse(is_byte_length('a', { "max": 0 }))
        print('OK - test_invalid_byte_length')
