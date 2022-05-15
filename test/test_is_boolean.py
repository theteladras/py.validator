import unittest

from pyvalidator.is_boolean import is_boolean
from . import print_test_ok


class TestIsBoolean(unittest.TestCase):

    def test_valid_booleans(self):
        for i in [
            'True',
            'False',
            'true',
            'false',
            '0',
            '1',
        ]:
            self.assertTrue(is_boolean(i))
        print_test_ok()

    def test_invalid_booleans(self):
        for i in [
            '1.0',
            '0.0',
            'true ',
            'yes',
        ]:
            self.assertFalse(is_boolean(i))
        print_test_ok()

    def test_valid_loosly_booleans(self):
        for i in [
            'true',
            'True',
            'TRUE',
            'false',
            'False',
            'FALSE',
            '0',
            '1',
            'yes',
            'Yes',
            'YES',
            'no',
            'No',
            'NO',
        ]:
            self.assertTrue(is_boolean(i, {"loose": True}))
        print_test_ok()

    def test_invalid_loosly_booleans(self):
        for i in [
            '1.0',
            '0.0',
            'true ',
            ' false',
        ]:
            self.assertFalse(is_boolean(i, {"loose": True}))
        print_test_ok()
