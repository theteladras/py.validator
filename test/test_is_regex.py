import unittest

from pyvalidator import *


class TestIsRegularExpression(unittest.TestCase):

    def valid_check(self, items, opts = {}):
        for item in items:
            self.assertTrue(is_regex(item, opts))

    def invalid_check(self, items, opts = {}):
        for item in items:
            self.assertFalse(is_regex(item, opts))

    def test_valid_regex(self):
        valid_items = [
            'A',
            '[\n]',
            '^([^\x00-\x1F\x7F-\x9F]+)<',
            'Hello World',
            'Hello\nworld',
            '[^a-z]{1:}',
            'A*AB',
            '.*ABA.?',
            '\d{5}(-\d{4})?',
            '//[^\r\n]*[\r\n]',
            '^test$',
            '^(0x)[0-9a-f]{40}$',
            '^(\3)?[0-9]{3}-[0-9]{4}$',
            '(?:(?:[^?+*{}()[\]\\|]+|\\.|\[(?:\^?\\.|\^[^\\]|[^\\^])))',
            '^(?:4[0-9]{12}(?:[0-9]{3,6})?|5[1-5][0-9]{14}|(222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|6(?:011|5[0-9][0-9])[0-9]{12,15}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11}|6[27][0-9]{14}|^(81[0-9]{14,17}))$',
            r'[\n]',
            r'^(\\3)?[0-9]{3}-[0-9]{4}$',
            r'boom\\',
            r'[\\]',
            r'^(0x)[0-9a-f]{40}$'
        ]
        self.valid_check(valid_items)
        print('OK - test_valid_regex')

    def test_invalid_regex(self):
        invalid_items = [
            '',
            '*',
            '**',
            '[]',
            'boom\\',
            '[0-9]++',
            '[asd',
            '?1',
            'AA(C)B)A',
            '[[a--z]{1:}',
            '\d{5}(-\d{4})???',
            '^(\\3)?[0-9]+{3}-[0-9]{4}$',
            '(?:(?:[^?+*{}()[\]\\|]+|\\.|\[(?:\^?\\.|\^[^\\]|[^\\^]))',
        ]
        self.invalid_check(invalid_items)
        print('OK - test_invalid_regex')

    def test_valid_regex_with_flags(self):
        valid_items = [
            r'/[\n]/g',
            '/[^a-z]/i',
            '/^([^\x00-\x1F\x7F-\x9F]+)</i',
            '/Hello World/m',
            r'/Hello\nworld/s',
            r'/BOOM\\/u',
            '/[^a-z]{1:}/y',
            '/.*ABA.?/d',
            '/asd\/asd/dy',
            '/(?:asd)!/imsu',
            '/^(0x)[0-9a-f]{40}$/'
        ]
        self.valid_check(valid_items, { "with_flags": True })
        print('OK - test_valid_regex_with_flags')

    def test_invalid_regex_with_flags(self):
        invalid_items = [
            '/^([^\x00-\x1F\x7F-\x9F]+)</e',
            '/Hello World/n',
            '[^fine]/n',
            '.+',
            '/Hello\nworld/s',
            '/BOOM\\/u',
        ]
        self.invalid_check(invalid_items, { "with_flags": True })
        print('OK - test_invalid_regex_with_flags')
