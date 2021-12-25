import unittest
from pyvalidator import *

class TestIsCurrency(unittest.TestCase):

    def test_valid_currency(self):
        self.assertTrue(is_currency('-$10,123.45'))
        self.assertTrue(is_currency('$10,123.45'))
        self.assertTrue(is_currency('$10123.45'))
        self.assertTrue(is_currency('10,123.45'))
        self.assertTrue(is_currency('10123.45'))
        self.assertTrue(is_currency('10,123'))
        self.assertTrue(is_currency('1,123,456'))
        self.assertTrue(is_currency('1123456'))
        self.assertTrue(is_currency('1.39'))
        self.assertTrue(is_currency('.03'))
        self.assertTrue(is_currency('0.10'))
        self.assertTrue(is_currency('$0.10'))
        self.assertTrue(is_currency('-$0.01'))
        self.assertTrue(is_currency('-$.99'))
        self.assertTrue(is_currency('$100,234,567.89'))
        self.assertTrue(is_currency('$10,123'))
        self.assertTrue(is_currency('10,123'))
        self.assertTrue(is_currency('-10123'))
        print('OK - test_valid_currency')

    def test_invalid_currency(self):
        self.assertFalse(is_currency('1.234'))
        self.assertFalse(is_currency('$1.1'))
        self.assertFalse(is_currency('$ 32.50'))
        self.assertFalse(is_currency('500$'))
        self.assertFalse(is_currency('.0001'))
        self.assertFalse(is_currency('$.001'))
        self.assertFalse(is_currency('$0.001'))
        self.assertFalse(is_currency('$12,34.56'))
        self.assertFalse(is_currency('123456,123,123456'))
        self.assertFalse(is_currency('123,4'))
        self.assertFalse(is_currency(',123'))
        self.assertFalse(is_currency('$-,123'))
        self.assertFalse(is_currency('$'))
        self.assertFalse(is_currency('.'))
        self.assertFalse(is_currency(','))
        self.assertFalse(is_currency('00'))
        self.assertFalse(is_currency('$-'))
        self.assertFalse(is_currency('$-,.'))
        self.assertFalse(is_currency('-'))
        self.assertFalse(is_currency('-$'))
        self.assertFalse(is_currency(''))
        self.assertFalse(is_currency('- $'))
        print('OK - test_invalid_currency')

    def test_valid_currency_dont_allow_decimal(self):
        self.assertTrue(is_currency('-$10,123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('$10,123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('$10123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('10,123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('10123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('10,123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('1,123,456', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('1123456', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('1', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('0', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('$0', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('-$0', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('$100,234,567', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('$10,123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('10,123', {
          "allow_decimal": False,
        }))
        self.assertTrue(is_currency('-10123', {
          "allow_decimal": False,
        }))
        print('OK - test_valid_currency_dont_allow_decimal')

    def test_invalid_currency_allow_decimal(self):
        self.assertFalse(is_currency('1.234', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$1.1', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$ 32.50', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('500$', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('.0001', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$.001', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$0.001', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$12,34.56', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('123456,123,123456', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('123,4', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency(',123', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$-,123', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('.', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency(',', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('00', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$-', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('$-,.', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('-', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('-$', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('', {
          "allow_decimal": False,
        }))
        self.assertFalse(is_currency('- $', {
          "allow_decimal": False,
        }))
        print('OK - test_invalid_currency_dont_allow_decimal')

    def test_valid_currency_digits_after_decimal(self):
        self.assertTrue(is_currency('-$10,123.4', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('$10,123.454', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('$10123.452', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('10,123.453', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('10123.450', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('10,123', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('1,123,456', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertTrue(is_currency('0.100', {
          "digits_after_decimal": [1, 3],
        }))
        print('OK - test_valid_currency_dont_allow_decimal')

    def test_invalid_currency_digits_after_decimal(self):
        self.assertFalse(is_currency('1.23', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('$1.13322', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('$ 32.50', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('500$', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('.0001', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('$.01', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('$0.01', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('$12,34.56', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('123456,123,123456', {
          "digits_after_decimal": [1, 3],
        }))
        self.assertFalse(is_currency('123,4', {
          "digits_after_decimal": [1, 3],
        }))
        print('OK - test_invalid_currency_digits_after_decimal')

    def test_valid_currency_require_symbol(self):
        self.assertTrue(is_currency('-$.99', {
          "require_symbol": True,
        }))
        self.assertTrue(is_currency('$100,234,567.89', {
          "require_symbol": True,
        }))
        self.assertTrue(is_currency('$1123456', {
          "require_symbol": True,
        }))
        print('OK - test_valid_currency_require_symbol')

    def test_invalid_currency_require_symbol(self):
        self.assertFalse(is_currency('1.23', {
          "require_symbol": True,
        }))
        self.assertFalse(is_currency('1.1', {
          "require_symbol": True,
        }))
        self.assertFalse(is_currency('500', {
          "require_symbol": True,
        }))
        self.assertFalse(is_currency('.0001', {
          "require_symbol": True,
        }))
        print('OK - test_invalid_currency_require_symbol')

    def test_valid_currency_add_symbol_prefix(self):
        self.assertTrue(is_currency('123,456.78', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertTrue(is_currency('¥6,954,231', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertTrue(is_currency('¥-10.03', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertTrue(is_currency('.03', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        print('OK - test_valid_currency_add_symbol_prefix')

    def test_invalid_currency_add_symbol_prefix(self):
        self.assertFalse(is_currency('1.234', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertFalse(is_currency('¥1.1', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertFalse(is_currency('5,00', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertFalse(is_currency('.0001', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        self.assertFalse(is_currency('¥.001', {
          "symbol": "¥",
          "negative_sign_before_digits": True,
        }))
        print('OK - test_invalid_currency_add_symbol_prefix')
