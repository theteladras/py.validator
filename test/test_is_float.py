import unittest

from pyvalidator.is_float import is_float
from . import print_test_ok


class TestIsFloat(unittest.TestCase):

    def test_valid_floats(self):
        for i in [
            '123',
            '123.',
            '123.123',
            '-123.123',
            '-0.123',
            '+0.123',
            '0.123',
            '.0',
            '-.123',
            '+.123',
            '01.123',
            '-0.11250738585072011e-307',
        ]:
            self.assertTrue(is_float(i))
        print_test_ok()

    def test_invalid_floats(self):
        for i in [
            '+',
            '-',
            '  ',
            '',
            '.',
            'foo',
            '20.foo',
            '2020-11-06T14:31:00.135Z',
        ]:
            self.assertFalse(is_float(i))
        print_test_ok()

    def test_valid_floats_locale_ar(self):
        for i in [
            '123',
            '123٫',
            '123٫123',
            '-123٫123',
            '-0٫123',
            '+0٫123',
            '0٫123',
            '٫0',
            '-٫123',
            '+٫123',
            '01٫123',
            '-0٫11250738585072011e-307',
        ]:
            self.assertTrue(is_float(i, {"locale": "ar"}))
        print_test_ok()

    def test_invalid_floats_locale_ar(self):
        for i in [
            '123,123',
            '123.123',
            '  ',
            '',
            '.',
            'foo',
            '20.foo',
            '2020-11-06T14:31:00.135Z',
        ]:
            self.assertFalse(is_float(i, {"locale": "ar"}))
        print_test_ok()
