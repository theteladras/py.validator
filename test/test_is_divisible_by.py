import unittest

from pyvalidator.is_divisible_by import is_divisible_by
from . import print_test_ok


class TestIsDivisibleBy(unittest.TestCase):

    def test_valid_divisible(self):
        for i in [
            ['2', 2],
            ['4', 2],
            ['100', 2],
            ['1000', 2],
        ]:
            self.assertTrue(is_divisible_by(*i))
        print_test_ok()

    def test_invalid_divisible(self):
        for i in [
            ['1', 2],
            ['2.5', 2],
            ['101', 2],
            ['foo', 2],
            ['', 2],
            ['2020-01-06T14:31:00.135Z', 2],
        ]:
            self.assertFalse(is_divisible_by(*i))
        print_test_ok()
