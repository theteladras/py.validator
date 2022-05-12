import unittest

from pyvalidator.is_uppercase import is_uppercase
from . import print_test_ok


class TestIsUppercase(unittest.TestCase):

    def test_valid_uppercase(self):
        for i in [
            'CCC',
            'UYTREWQ',
            'ASD123',
            'HELLO WORLD',
            '   .',
        ]:
            self.assertTrue(is_uppercase(i))
        print_test_ok()

    def test_invalid_uppercase(self):
        for i in [
            'hello world',
            'HELLO WORLd',
            'asd123',
        ]:
            self.assertFalse(is_uppercase(i))
        print_test_ok()
