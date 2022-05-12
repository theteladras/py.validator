import unittest

from pyvalidator.is_int import is_int
from . import print_test_ok


class TestIsInt(unittest.TestCase):

    def test_valid_ints(self):
        for i in [
            '13',
            '123',
            '0',
            '-0',
            '+1',
            '01',
            '-01',
            '000',
        ]:
            self.assertTrue(is_int(i))
        print_test_ok()

    def test_invalid_ints(self):
        for i in [
            '100e10',
            '123.123',
            '   ',
            '',
            '.',
            'foo',
        ]:
            self.assertFalse(is_int(i))
        print_test_ok()

    def test_valid_ints_dont_allow_leading_zeroes(self):
        for i in [
            '13',
            '11',
            '123',
            '0',
            '-0',
            '+1',
        ]:
            self.assertTrue(is_int(i, {"allow_leading_zeroes": False}))
        print_test_ok()

    def test_invalid_ints_dont_allow_leading_zeroes(self):
        for i in [
            '01',
            '-01',
            '000',
            '100e10',
            '123.11',
            'foo',
            '   ',
            '',
            '\n',
            '\t',
        ]:
            self.assertFalse(is_int(i, {"allow_leading_zeroes": False}))
        print_test_ok()

    def test_fail_ints(self):
        for i in [
            None,
            {},
        ]:
            self.assertRaises(Exception, is_int, i)
        print_test_ok()
