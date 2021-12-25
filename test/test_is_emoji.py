import unittest
from pyvalidator import *

class TestIsEmoji(unittest.TestCase):

    def test_valid_emoji(self):
        self.assertTrue(is_emoji('🌼'))
        self.assertTrue(is_emoji('😀'))
        self.assertTrue(is_emoji('😃'))
        self.assertTrue(is_emoji('😎'))
        self.assertTrue(is_emoji('🍗'))
        self.assertTrue(is_emoji('🌯'))
        self.assertTrue(is_emoji('🍔'))
        self.assertTrue(is_emoji('🍗🍗🍗'))
        self.assertTrue(is_emoji('💪'))
        self.assertTrue(is_emoji('🇷🇸'))
        self.assertTrue(is_emoji('🇺🇸'))
        self.assertTrue(is_emoji('🇦🇪'))
        self.assertTrue(is_emoji('🇮🇱'))
        self.assertTrue(is_emoji('🇮🇹'))
        self.assertTrue(is_emoji('🇹🇷'))
        self.assertTrue(is_emoji('🇦🇷'))
        self.assertTrue(is_emoji('🇧🇧'))
        print('OK - test_valid_emoji')

    def test_invalid_emoji(self):
        self.assertFalse(is_emoji(''))
        self.assertFalse(is_emoji(' '))
        self.assertFalse(is_emoji('\n'))
        self.assertFalse(is_emoji('-1💪'))
        self.assertFalse(is_emoji('💪65536'))
        self.assertFalse(is_emoji('655369'))
        self.assertFalse(is_emoji('.'))
        self.assertFalse(is_emoji('😃.😃'))
        self.assertFalse(is_emoji('asd'))
        self.assertFalse(is_emoji('\U000027B00'))
        print('OK - test_invalid_emoji')

    def test_valid_emoji_by_omited_dot(self):
        self.assertTrue(is_emoji('.🌼', { "omit_rule": r'[.]' }))
        self.assertTrue(is_emoji('😀.', { "omit_rule": r'[.]' }))
        self.assertTrue(is_emoji('😀.🌼', { "omit_rule": r'[.]' }))
        self.assertTrue(is_emoji('😀.🌼.😀', { "omit_rule": r'[.]' }))
        self.assertTrue(is_emoji('😀.-🌼.-😀', { "omit_rule": r'[.-]' }))
        print('OK - test_valid_emoji_by_omited_dot')
