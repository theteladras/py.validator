import unittest

from pyvalidator.is_multibyte import is_multibyte
from . import print_test_ok


class TestIsMultiByte(unittest.TestCase):

    def test_valid_multibyte(self):
        for i in [
            'ひらがな・カタカナ、．漢字',
            'あいうえお foobar',
            'ｶﾀｶﾅ',
            '中文',
            'test＠example.com',
            '1234abcDEｘｙｚ',
        ]:
            self.assertTrue(is_multibyte(i))
        print_test_ok()

    def test_invalid_multibyte(self):
        for i in [
            'abc',
            'abc123',
            '<>@" *.',
        ]:
            self.assertFalse(is_multibyte(i))
        print_test_ok()
