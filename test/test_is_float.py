import unittest
from validator import *

class TestIsFloat(unittest.TestCase):

    def test_valid_floats(self):
        self.assertTrue(is_float('123'))
        self.assertTrue(is_float('123.'))
        self.assertTrue(is_float('123.123'))
        self.assertTrue(is_float('-123.123'))
        self.assertTrue(is_float('-0.123'))
        self.assertTrue(is_float('+0.123'))
        self.assertTrue(is_float('0.123'))
        self.assertTrue(is_float('.0'))
        self.assertTrue(is_float('-.123'))
        self.assertTrue(is_float('+.123'))
        self.assertTrue(is_float('01.123'))
        self.assertTrue(is_float('-0.11250738585072011e-307'))
        print('OK - test_valid_floats')

    def test_invalid_floats(self):
        self.assertFalse(is_float('+'))
        self.assertFalse(is_float('-'))
        self.assertFalse(is_float('  '))
        self.assertFalse(is_float(''))
        self.assertFalse(is_float('.'))
        self.assertFalse(is_float('foo'))
        self.assertFalse(is_float('20.foo'))
        self.assertFalse(is_float('2020-11-06T14:31:00.135Z'))
        print('OK - test_invalid_floats')

    def test_valid_floats_locale_ar(self):
        self.assertTrue(is_float('123', { "locale": "ar" }))
        self.assertTrue(is_float('123٫', { "locale": "ar" }))
        self.assertTrue(is_float('123٫123', { "locale": "ar" }))
        self.assertTrue(is_float('-123٫123', { "locale": "ar" }))
        self.assertTrue(is_float('-0٫123', { "locale": "ar" }))
        self.assertTrue(is_float('+0٫123', { "locale": "ar" }))
        self.assertTrue(is_float('0٫123', { "locale": "ar" }))
        self.assertTrue(is_float('٫0', { "locale": "ar" }))
        self.assertTrue(is_float('-٫123', { "locale": "ar" }))
        self.assertTrue(is_float('+٫123', { "locale": "ar" }))
        self.assertTrue(is_float('01٫123', { "locale": "ar" }))
        self.assertTrue(is_float('-0٫11250738585072011e-307', { "locale": "ar" }))
        print('OK - test_valid_floats_locale_ar')

    def test_invalid_floats_locale_ar(self):
        self.assertFalse(is_float('123,123', { "locale": "ar" }))
        self.assertFalse(is_float('123.123', { "locale": "ar" }))
        self.assertFalse(is_float('  ', { "locale": "ar" }))
        self.assertFalse(is_float('', { "locale": "ar" }))
        self.assertFalse(is_float('.', { "locale": "ar" }))
        self.assertFalse(is_float('foo', { "locale": "ar" }))
        self.assertFalse(is_float('20.foo', { "locale": "ar" }))
        self.assertFalse(is_float('2020-11-06T14:31:00.135Z', { "locale": "ar" }))
        print('OK - test_invalid_floats_locale_ar')
