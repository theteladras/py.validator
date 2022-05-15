import unittest

from pyvalidator.is_lowercase import is_lowercase
from . import print_test_ok


class TestIsLowercase(unittest.TestCase):

    def test_valid_lowercase(self):
        for i in [
            'ccc',
            'qwerty',
            'asd123',
            'hello world',
            '   .',
        ]:
            self.assertTrue(is_lowercase(i))
        print_test_ok()

    def test_invalid_lowercase(self):
        for i in [
            'hello WoRLD',
            'HELLO WORLd',
            'ASD123',
        ]:
            self.assertFalse(is_lowercase(i))
        print_test_ok()
