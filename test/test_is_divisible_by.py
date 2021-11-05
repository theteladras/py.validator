import unittest
from validator import *

class TestIsDivisibleBy(unittest.TestCase):

    def test_valid_divisible(self):
        self.assertTrue(is_divisible_by('2', 2))
        self.assertTrue(is_divisible_by('4', 2))
        self.assertTrue(is_divisible_by('100', 2))
        self.assertTrue(is_divisible_by('1000', 2))
        print('OK - test_valid_divisible')

    def test_invalid_divisible(self):
        self.assertFalse(is_divisible_by('1', 2))
        self.assertFalse(is_divisible_by('2.5', 2))
        self.assertFalse(is_divisible_by('101', 2))
        self.assertFalse(is_divisible_by('foo', 2))
        self.assertFalse(is_divisible_by('', 2))
        self.assertFalse(is_divisible_by('2020-01-06T14:31:00.135Z', 2))
        print('OK - test_invalid_divisible')
