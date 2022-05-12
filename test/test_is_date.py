import unittest

from pyvalidator.is_date import is_date
from . import print_test_ok


class TestIsDate(unittest.TestCase):

    def test_valid_date(self):
        for i in [
            '2020/02/29',
            '2004-02-29',
            '2011-12-13',
            '1911-12-13',
        ]:
            self.assertTrue(is_date(i))
        print_test_ok()

    def test_invalid_date(self):
        for i in [
            '15072002',
            '2020-02-30',
            '2011-12/13',
            '2011/2/13',
            '',
            'asd',
        ]:
            self.assertFalse(is_date(i))
        print_test_ok()

    def test_valid_date_custom_format(self):
        for i in [
            ['12/20/19', {"format": "MM/DD/YY"}],
            ['12/20/19', {"format": "mm/dd/yy"}],
            ['02-04-04', {"format": "MM/DD/YY"}],
            ['02-04-04', {"format": "mm-DD-yy"}],
        ]:
            self.assertTrue(is_date(*i))
        print_test_ok()

    def test_invalid_date_custom_format(self):
        for i in [
            ['2/20/29', {"format": "MM/DD/YY"}],
            ['02/20/29', {"format": "MM/DD/YYYY"}],
        ]:
            self.assertFalse(is_date(*i))
        print_test_ok()

    def test_valid_date_strict_mode(self):
        for i in [
            '2020/02/29',
            '1920/02/29',
        ]:
            self.assertTrue(is_date(i, {"strict_mode": True}))
        print_test_ok()

    def test_invalid_date_strict_mode(self):
        for i in [
            '15072002',
            '2020-02-30',
            '2004-02-29',
            '2011-12/13',
        ]:
            self.assertFalse(is_date(i, {"strict_mode": True}))
        print_test_ok()

    def test_valid_date_strict_mode_hyphen_format(self):
        for i in [
            '2020-02-29',
        ]:
            self.assertTrue(is_date(i, {"strict_mode": True, "format": 'YYYY-MM-DD'}))
        print_test_ok()

    def test_invalid_date_strict_mode_hyphen_format(self):
        for i in [
            '2020/02/29',
            '2019/09/30',
        ]:
            self.assertFalse(is_date(i, {"strict_mode": True, "format": 'YYYY-MM-DD'}))
        print_test_ok()

    def test_valid_date_custom_delimiter(self):
        for i in [
            ['2020.02.29', {"delimiters": ['.']}],
            ['2020,02,29', {"delimiters": [',']}],
            ['02,11,2019', {"delimiters": [','], "format": 'DD/MM/YYYY'}],
            ['02,11,19', {"delimiters": [','], "format": 'DD/MM/YY'}],
            ['02|11|19', {"delimiters": ['|'], "format": 'YY|MM|DD'}],
            ['02;11;19', {"delimiters": [';'], "format": 'YY;MM;DD'}],
            ['02:11:19', {"delimiters": [':'], "format": 'YY:MM:DD'}],
        ]:
            self.assertTrue(is_date(*i))
        print_test_ok()

    def test_invalid_date_custom_delimiter(self):
        for i in [
            ['2020,02,29', {"delimiters": ['.']}],
            ['2020.02.29', {"delimiters": [',']}],
            ['02,11,2019', {"delimiters": [','], "format": 'DD/MM/YY'}],
        ]:
            self.assertFalse(is_date(*i))
        print_test_ok()

    def test_valid_date_custom_delimiter_strict_mode(self):
        self.assertTrue(is_date('2020.02.29', {"delimiters": ['.'], "strict_mode": True, "format": 'YYYY.MM.DD'}))
        self.assertTrue(is_date('02.29.20', {"delimiters": ['.'], "strict_mode": True, "format": 'MM.DD.YY'}))
        print_test_ok()

    def test_invalid_date_custom_delimiter_strict_mode(self):
        self.assertFalse(is_date('2020.02.29', {"delimiters": ['.'], "strict_mode": True, "format": 'YYYY,MM,DD'}))
        print_test_ok()

    def test_rais_error_for_unsuported_date_format(self):
        for i in [
            ['2020/02/29', {"format": 'MM/YY/DD'}],
            ['2020/02/29', {"format": ''}],
        ]:
            self.assertRaises(Exception, is_date, i)
        print_test_ok()
