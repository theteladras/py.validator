import unittest

from pyvalidator.is_byte_length import is_byte_length
from . import print_test_ok


class TestIsByteLength(unittest.TestCase):

    def test_valid_byte_length_min_2(self):
        for i in [
            'abc',
            'de',
            'abcd',
            'ｇｍａｉｌ',
        ]:
            self.assertTrue(is_byte_length(i, {"min": 2}))
        print_test_ok()

    def test_invalid_byte_length_min_2(self):
        for i in [
            '',
            'a',
        ]:
            self.assertFalse(is_byte_length(i, {"min": 2}))
        print_test_ok()

    def test_valid_byte_length_min_2_max_3(self):
        for i in [
            'abc',
            'de',
            'ｇ',
        ]:
            self.assertTrue(is_byte_length(i, {"min": 2, "max": 3}))
        print_test_ok()

    def test_invalid_byte_length_min_2_max_3(self):
        for i in [
            '',
            'a',
            'abcd',
            'ｇｍ',
        ]:
            self.assertFalse(is_byte_length(i, {"min": 2, "max": 3}))
        print_test_ok()

    def test_valid_byte_length_max_0(self):
        self.assertTrue(is_byte_length('', { "max": 0 }))
        print_test_ok()

    def test_invalid_byte_length_max_0(self):
        for i in [
            'g',
            'a',
        ]:
            self.assertFalse(is_byte_length(i, {"max": 0}))
        print_test_ok()
