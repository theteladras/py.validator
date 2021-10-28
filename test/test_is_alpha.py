import unittest
import validator

class TestIsAlpha(unittest.TestCase):

    def test_valid_alpha_strings(self):
        self.assertTrue(validator.is_alpha('abc'))
        self.assertTrue(validator.is_alpha('ABC'))
        self.assertTrue(validator.is_alpha('FoObar'))
        print('OK - test_valid_alpha_strings')

    def test_invalid_alpha_strings(self):
        self.assertFalse(validator.is_alpha('abc1'))
        self.assertFalse(validator.is_alpha('  foo  '))
        self.assertFalse(validator.is_alpha('FÜübar'))
        self.assertFalse(validator.is_alpha('Jön'))
        print('OK - test_invalid_alpha_strings')

    def test_valid_alpha_strings_with_ignored_characters(self):
        self.assertTrue(validator.is_alpha('en-US', 'en-US', { "ignore": '- /' }))
        self.assertTrue(validator.is_alpha('this is a valid alpha string', 'en-US', { "ignore": '- /' }))
        self.assertTrue(validator.is_alpha('us/usa', 'en-US', { "ignore": '- /' }))
        print('OK - test_valid_alpha_strings_with_ignored_characters')

    def test_invalid_alpha_strings_with_ignored_characters(self):
        self.assertFalse(validator.is_alpha('1. this is not a valid alpha string', 'en-US', { "ignore": '- /' }))
        self.assertFalse(validator.is_alpha('this$is also not a valid.alpha string', 'en-US', { "ignore": '- /' }))
        self.assertFalse(validator.is_alpha('this is also not a valid alpha string.', 'en-US', { "ignore": '- /' }))
        print('OK - test_invalid_alpha_strings_with_ignored_characters')

    def test_should_throw_for_invalid_ignore_matcher(self):
        self.assertRaises(Exception, validator.is_alpha, ['this is also not a valid alpha string.', 'en-US', { "ignore": 123 }])
        print('OK - test_should_throw_for_invalid_ignore_matcher')
