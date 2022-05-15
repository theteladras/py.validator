import unittest

from pyvalidator.is_emoji import is_emoji
from . import print_test_ok


class TestIsEmoji(unittest.TestCase):

    def test_valid_emoji(self):
        for i in [
            '🌼', '😀', '😃', '😎', '🍗', '🌯', '🍔', '🍗🍗🍗', '💪', '🇷🇸', '🇺🇸',
            '🇦🇪', '🇮🇱', '🇮🇹', '🇹🇷', '🇦🇷', '🇧🇧',
        ]:
            self.assertTrue(is_emoji(i))
        print_test_ok()

    def test_invalid_emoji(self):
        for i in [
            '',
            ' ',
            '\n',
            '-1💪',
            '💪65536',
            '655369',
            '.',
            '😃.😃',
            'asd',
            '\U000027B00',
        ]:
            self.assertFalse(is_emoji(i))
        print_test_ok()

    def test_valid_emoji_by_omitted_dot(self):
        for i in [
            ['.🌼', {"omit_rule": r'[.]'}],
            ['😀.', {"omit_rule": r'[.]'}],
            ['😀.🌼', {"omit_rule": r'[.]'}],
            ['😀.🌼.😀', {"omit_rule": r'[.]'}],
            ['😀.-🌼.-😀', {"omit_rule": r'[.-]'}],
        ]:
            self.assertTrue(is_emoji(*i))
        print_test_ok()
