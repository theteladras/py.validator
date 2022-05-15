import unittest

from pyvalidator.is_number import is_number
from . import print_test_ok


class TestIsNumber(unittest.TestCase):

    def test_valid_numbers(self):
        for i in [
            '13',
            '123',
            '0.11',
            '-0',
            '+1.1',
            '012',
            '-013',
            '000',
            '123.123',
            '-123٫123',
            '+0٫123',
            '-0.11250738585072011e-307',
        ]:
            self.assertTrue(is_number(i))
        print_test_ok()

    def test_invalid_numbers(self):
        for i in [
            '123,123,asd',
            'asd',
            '.',
            '   ',
            '',
            ',',
            'foofoo',
            '2^3',
            '2+3',
        ]:
            self.assertFalse(is_number(i))
        print_test_ok()
