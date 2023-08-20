import unittest

from pyvalidator.is_iso6391 import is_iso6391
from . import print_test_ok


class TestIsISO6391(unittest.TestCase):

    def test_valid_iso6391(self):
        for i in ['ay', 'az', 'ba', 'be', 'bg']:
            self.assertTrue(is_iso6391(i), i)
        print_test_ok()

    def test_invalid_iso6391(self):
        for i in ['aj', 'al', 'pe', 'pf', 'abc', '123', '']:
            self.assertFalse(is_iso6391(i), i)
        print_test_ok()
