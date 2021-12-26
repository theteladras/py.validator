import unittest
from pyvalidator import *

class TestIsDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(is_date('2020/02/29'))
        self.assertTrue(is_date('2004-02-29'))
        self.assertTrue(is_date('2011-12-13'))
        self.assertTrue(is_date('1911-12-13'))
        print('OK - test_valid_date')

    def test_invalid_date(self):
        self.assertFalse(is_date('15072002'))
        self.assertFalse(is_date('2020-02-30'))
        self.assertFalse(is_date('2011-12/13'))
        self.assertFalse(is_date('2011/2/13'))
        self.assertFalse(is_date(''))
        self.assertFalse(is_date('asd'))
        print('OK - test_invalid_date')

    def test_valid_date_custom_format(self):
        self.assertTrue(is_date('12/20/19', { "format": "MM/DD/YY" }))
        self.assertTrue(is_date('12/20/19', { "format": "mm/dd/yy" }))
        self.assertTrue(is_date('02-04-04', { "format": "MM/DD/YY" }))
        self.assertTrue(is_date('02-04-04', { "format": "mm-DD-yy" }))
        print('OK - test_valid_date_custom_format')

    def test_invalid_date_custom_format(self):
        self.assertFalse(is_date('2/20/29', { "format": "MM/DD/YY" }))
        self.assertFalse(is_date('02/20/29', { "format": "MM/DD/YYYY" }))
        print('OK - test_invalid_date_custom_format')

    def test_valid_date_strict_mode(self):
        self.assertTrue(is_date('2020/02/29', { "strict_mode": True }))
        self.assertTrue(is_date('1920/02/29', { "strict_mode": True }))
        print('OK - test_valid_date_strict_mode')

    def test_invalid_date_strict_mode(self):
        self.assertFalse(is_date('15072002', { "strict_mode": True }))
        self.assertFalse(is_date('2020-02-30', { "strict_mode": True }))
        self.assertFalse(is_date('2004-02-29', { "strict_mode": True }))
        self.assertFalse(is_date('2011-12/13', { "strict_mode": True }))
        print('OK - test_invalid_date_strict_mode')

    def test_valid_date_strict_mode_hyphen_format(self):
        self.assertTrue(is_date('2020-02-29', { "strict_mode": True, "format": 'YYYY-MM-DD' }))
        print('OK - test_valid_date_strict_mode_hyphen_format')

    def test_invalid_date_strict_mode_hyphen_format(self):
        self.assertFalse(is_date('2020/02/29', { "strict_mode": True, "format": 'YYYY-MM-DD' }))
        self.assertFalse(is_date('2019/09/30', { "strict_mode": True, "format": 'YYYY-MM-DD' }))
        print('OK - test_invalid_date_strict_mode_hyphen_format')

    def test_valid_date_custom_delimiter(self):
        self.assertTrue(is_date('2020.02.29', { "delimiters": ['.'] }))
        self.assertTrue(is_date('2020,02,29', { "delimiters": [','] }))
        self.assertTrue(is_date('02,11,2019', { "delimiters": [','], "format": 'DD/MM/YYYY' }))
        self.assertTrue(is_date('02,11,19', { "delimiters": [','], "format": 'DD/MM/YY' }))
        self.assertTrue(is_date('02|11|19', { "delimiters": ['|'], "format": 'YY|MM|DD' }))
        self.assertTrue(is_date('02;11;19', { "delimiters": [';'], "format": 'YY;MM;DD' }))
        self.assertTrue(is_date('02:11:19', { "delimiters": [':'], "format": 'YY:MM:DD' }))
        print('OK - test_valid_date_custom_delimiter')

    def test_invalid_date_custom_delimiter(self):
        self.assertFalse(is_date('2020,02,29', { "delimiters": ['.'] }))
        self.assertFalse(is_date('2020.02.29', { "delimiters": [','] }))
        self.assertFalse(is_date('02,11,2019', { "delimiters": [','], "format": 'DD/MM/YY' }))
        print('OK - test_invalid_date_custom_delimiter')

    def test_valid_date_custom_delimiter_strict_mode(self):
        self.assertTrue(is_date('2020.02.29', { "delimiters": ['.'], "strict_mode": True, "format": 'YYYY.MM.DD' }))
        self.assertTrue(is_date('02.29.20', { "delimiters": ['.'], "strict_mode": True, "format": 'MM.DD.YY' }))
        print('OK - test_valid_date_custom_delimiter_strict_mode')

    def test_invalid_date_custom_delimiter_strict_mode(self):
        self.assertFalse(is_date('2020.02.29', { "delimiters": ['.'], "strict_mode": True, "format": 'YYYY,MM,DD' }))
        print('OK - test_invalid_date_custom_delimiter_strict_mode')

    def test_rais_error_for_unsuported_date_format(self):
        self.assertRaises(Exception, is_date, ['2020/02/29', { "format": 'MM/YY/DD' }])
        self.assertRaises(Exception, is_date, ['2020/02/29', { "format": '' }])
        print('OK - test_rais_error_for_unsuported_date_format')
