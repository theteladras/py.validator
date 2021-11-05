import unittest
from validator import *

class TestIsAlpha(unittest.TestCase):

    def test_valid_alpha_strings(self):
        self.assertTrue(is_alpha('abc'))
        self.assertTrue(is_alpha('ABC'))
        self.assertTrue(is_alpha('FoObar'))
        print('OK - test_valid_alpha_strings')

    def test_invalid_alpha_strings(self):
        self.assertFalse(is_alpha('abc1'))
        self.assertFalse(is_alpha('  foo  '))
        self.assertFalse(is_alpha('FÜübar'))
        self.assertFalse(is_alpha('Jön'))
        print('OK - test_invalid_alpha_strings')

    def test_valid_alpha_strings_with_ignored_characters(self):
        self.assertTrue(is_alpha('en-US', 'en-US', { "ignore": '- /' }))
        self.assertTrue(is_alpha('this is a valid alpha string', 'en-US', { "ignore": '- /' }))
        self.assertTrue(is_alpha('us/usa', 'en-US', { "ignore": '- /' }))
        print('OK - test_valid_alpha_strings_with_ignored_characters')

    def test_invalid_alpha_strings_with_ignored_characters(self):
        self.assertFalse(is_alpha('1. this is not a valid alpha string', 'en-US', { "ignore": '- /' }))
        self.assertFalse(is_alpha('this$is also not a valid.alpha string', 'en-US', { "ignore": '- /' }))
        self.assertFalse(is_alpha('this is also not a valid alpha string.', 'en-US', { "ignore": '- /' }))
        print('OK - test_invalid_alpha_strings_with_ignored_characters')

    def test_should_throw_for_invalid_ignore_matcher(self):
        self.assertRaises(Exception, is_alpha, ['this is also not a valid alpha string.', 'en-US', { "ignore": 123 }])
        print('OK - test_should_throw_for_invalid_ignore_matcher')
