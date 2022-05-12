import unittest

from pyvalidator.is_hexadecimal import is_hexadecimal
from . import print_test_ok


class TestIsHexadecimal(unittest.TestCase):

    def test_valid_hexadecimal(self):
        for i in [
            'AA',
            'deadBEEF',
            'ff0044',
            '0xff0044',
            '0XfF0044',
            '0x0123456789abcDEF',
            '0X0123456789abcDEF',
            '0hfedCBA9876543210',
            '0HfedCBA9876543210',
            '0123456789abcDEF',
        ]:
            self.assertTrue(is_hexadecimal(i))
        print_test_ok()

    def test_invalid_hexadecimal(self):
        for i in [
            '',
            '.',
            '..',
            'AA/',
            'A A',
            'abcdefg',
            '0xa2h',
            '0xa20x',
            '0x0123456789abcDEFq',
            '0hfedCBA9876543210q',
            '01234q56789abcDEF',
        ]:
            self.assertFalse(is_hexadecimal(i))
        print_test_ok()
