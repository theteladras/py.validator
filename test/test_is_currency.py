import unittest

from pyvalidator.is_currency import is_currency
from . import print_test_ok


class TestIsCurrency(unittest.TestCase):

    def test_valid_currency(self):
        for i in [
            '-$10,123.45',
            '$10,123.45',
            '$10123.45',
            '10,123.45',
            '10123.45',
            '10,123',
            '1,123,456',
            '1123456',
            '1.39',
            '.03',
            '0.10',
            '$0.10',
            '-$0.01',
            '-$.99',
            '$100,234,567.89',
            '$10,123',
            '10,123',
            '-10123',
        ]:
            self.assertTrue(is_currency(i))
        print_test_ok()

    def test_invalid_currency(self):
        for i in [
            '1.234',
            '$1.1',
            '$ 32.50',
            '500$',
            '.0001',
            '$.001',
            '$0.001',
            '$12,34.56',
            '123456,123,123456',
            '123,4',
            ',123',
            '$-,123',
            '$',
            '.',
            ',',
            '00',
            '$-',
            '$-,.',
            '-',
            '-$',
            '',
            '- $',
        ]:
            self.assertFalse(is_currency(i))
        print_test_ok()

    def test_valid_currency_dont_allow_decimal(self):
        for i in [
            '-$10,123',
            '$10,123',
            '$10123',
            '10,123',
            '10123',
            '10,123',
            '1,123,456',
            '1123456',
            '1',
            '0',
            '$0',
            '-$0',
            '$100,234,567',
            '$10,123',
            '10,123',
            '-10123',
        ]:
            self.assertTrue(is_currency(i, {"allow_decimal": False}))
        print_test_ok()

    def test_invalid_currency_allow_decimal(self):
        for i in [
            '1.234',
            '$1.1',
            '$ 32.50',
            '500$',
            '.0001',
            '$.001',
            '$0.001',
            '$12,34.56',
            '123456,123,123456',
            '123,4',
            ',123',
            '$-,123',
            '$',
            '.',
            ',',
            '00',
            '$-',
            '$-,.',
            '-',
            '-$',
            '',
            '- $',
        ]:
            self.assertFalse(is_currency(i, {"allow_decimal": False}))
        print_test_ok()

    def test_valid_currency_digits_after_decimal(self):
        for i in [
            '-$10,123.4',
            '$10,123.454',
            '$10123.452',
            '10,123.453',
            '10123.450',
            '10,123',
            '1,123,456',
            '0.100',
        ]:
            self.assertTrue(is_currency(i, {"digits_after_decimal": [1, 3]}))
        print_test_ok()

    def test_invalid_currency_digits_after_decimal(self):
        for i in [
            '1.23',
            '$1.13322',
            '$ 32.50',
            '500$',
            '.0001',
            '$.01',
            '$0.01',
            '$12,34.56',
            '123456,123,123456',
            '123,4',
        ]:
            self.assertFalse(is_currency(i, {"digits_after_decimal": [1, 3]}))
        print_test_ok()

    def test_valid_currency_require_symbol(self):
        for i in [
            '-$.99',
            '$100,234,567.89',
            '$1123456',
        ]:
            self.assertTrue(is_currency(i, {"require_symbol": True}))
        print_test_ok()

    def test_invalid_currency_require_symbol(self):
        for i in [
            '1.23',
            '1.1',
            '500',
            '.0001',
        ]:
            self.assertFalse(is_currency(i, {"require_symbol": True}))
        print_test_ok()

    def test_valid_currency_add_symbol_prefix(self):
        for i in [
            '123,456.78',
            '¥6,954,231',
            '¥-10.03',
            '.03',
        ]:
            self.assertTrue(is_currency(i, {"symbol": "¥", "negative_sign_before_digits": True}))
        print_test_ok()

    def test_invalid_currency_add_symbol_prefix(self):
        for i in [
            '1.234',
            '¥1.1',
            '5,00',
            '.0001',
            '¥.001',
        ]:
            self.assertFalse(is_currency(i, {"symbol": "¥", "negative_sign_before_digits": True}))
        print_test_ok()
