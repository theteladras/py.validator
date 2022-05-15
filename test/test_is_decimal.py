import unittest

from pyvalidator.is_decimal import is_decimal
from . import print_test_ok


class TestIsDecimal(unittest.TestCase):

    def test_valid_decimal(self):
        for i in [
            '123',
            '00123',
            '-00123',
            '0',
            '-0',
            '+123',
            '0.01',
            '.1',
            '1.0',
            '-.25',
            '-0',
            '0.0000000000001',
        ]:
            self.assertTrue(is_decimal(i))
        print_test_ok()

    def test_invalid_decimal(self):
        for i in [
            '0,01',
            ',1',
            '1,0',
            '-,25',
            '0,0000000000001',
            '0٫01',
            '٫1',
            '1٫0',
            '-٫25',
            '0٫0000000000001',
            '....',
            ' ',
            '-',
            '+',
            '.',
            '0.1a',
            'a',
            '\n',
        ]:
            self.assertFalse(is_decimal(i))
        print_test_ok()

    def test_valid_decimal_locale_en_au(self):
        for i in [
            '123',
            '00123',
            '-00123',
            '0',
            '-0',
            '+123',
            '0.01',
            '.1',
            '1.0',
            '-.25',
            '-0',
            '0.0000000000001',
        ]:
            self.assertTrue(is_decimal(i, {"locale": "en-AU"}))
        print_test_ok()

    def test_invalid_decimal_locale_en_au(self):
        for i in [
            '0,01',
            ',1',
            '1,0',
            '-,25',
            '0,0000000000001',
            '0٫01',
            '٫1',
            '1٫0',
            '-٫25',
            '0٫0000000000001',
            '....',
            ' ',
            '-',
            '+',
            '.',
            '0.1a',
            'a',
            '\n',
        ]:
            self.assertFalse(is_decimal(i, {"locale": "en-AU"}))
        print_test_ok()

    def test_valid_decimal_locale_ar(self):
        for i in [
            '123',
            '00123',
            '-00123',
            '0٫01',
            '٫1',
            '1٫0',
            '-٫25',
        ]:
            self.assertTrue(is_decimal(i, {"locale": "ar"}))
        print_test_ok()

    def test_invalid_decimal_locale_ar(self):
        for i in [
            '0.01',
            '.1',
            '1.0',
            '-.25',
            '0.0000000000001',
            '0.01',
            '.1',
            '1.0',
            '-.25',
            '0.0000000000001',
        ]:
            self.assertFalse(is_decimal(i, {"locale": "ar"}))
        print_test_ok()

    def test_valid_decimal_locale_force_decimal(self):
        for i in [
            '0.01',
            '.1',
            '1.0',
            '-.25',
            '0.0000000000001',
        ]:
            self.assertTrue(is_decimal(i, {"force_decimal": True}))
        print_test_ok()

    def test_invalid_decimal_locale_force_decimal(self):
        for i in [
            '-0',
            '123',
            '00123',
            '0',
            '+123',
        ]:
            self.assertFalse(is_decimal(i, {"force_decimal": True}))
        print_test_ok()

    def test_valid_decimal_locale_decimal_digits_2_3(self):
        for i in [
            '123',
            '00123',
            '-00123',
            '0',
            '-0',
            '+123',
            '-.255',
        ]:
            self.assertTrue(is_decimal(i, {"decimal_digits": "2,3"}))
        print_test_ok()

    def test_invalid_decimal_locale_decimal_digits_2_3(self):
        for i in [
            '0.0000000000001',
            '0.0',
            '.1',
            '1.0',
            '-.2564',
            '0.0',
            '٫1',
            '1٫0',
            '-٫25',
        ]:
            self.assertFalse(is_decimal(i, {"decimal_digits": "2,3"}))
        print_test_ok()
