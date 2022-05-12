import unittest

from pyvalidator.is_octal import is_octal
from . import print_test_ok


class TestIsOctal(unittest.TestCase):

    def test_valid_octal(self):
        for i in [
            '076543210',
            '0o01234567',
        ]:
            self.assertTrue(is_octal(i))
        print_test_ok()

    def test_invalid_octal(self):
        for i in [
            '',
            '.',
            '/',
            '999',
            'abcdefg',
            '012345678',
            '012345670c',
            '00c12345670c',
        ]:
            self.assertFalse(is_octal(i))
        print_test_ok()
