import unittest

from pyvalidator.is_port import is_port
from . import print_test_ok


class TestIsPort(unittest.TestCase):

    def test_valid_port(self):
        for i in [
            '0',
            '22',
            '80',
            '443',
            '5000',
            '8000',
            '65535',
        ]:
            self.assertTrue(is_port(i))
        print_test_ok()

    def test_invalid_port(self):
        for i in [
            '',
            '-1',
            '65536',
            '655369',
            '.',
        ]:
            self.assertFalse(is_port(i))
        print_test_ok()
