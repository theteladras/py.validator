import unittest

from pyvalidator import *


class TestIsCssUnit(unittest.TestCase):

    def valid_check(self, items):
        for item in items:
            self.assertTrue(is_css_unit(item))

    def invalid_check(self, items):
        for item in items:
            self.assertFalse(is_css_unit(item))

    def test_valid_css_unit(self):
        valid_items = [
            '-9px',
            '0.9px',
            '.9px',
            '-9em',
            '0.9em',
            '.9em',
            '5%',
            '-5%',
            '-0.5%',
            '0',
            '9ex',
            '9ch',
            '9rem',
            '9vw',
            '9vh',
            '9vmin',
            '3vmax',
            '-1cm',
            '1mm',
            '1.1in',
            '1.1pt',
            '1.1pc',
        ]
        self.valid_check(valid_items)
        print('OK - test_valid_css_unit')

    def test_invalid_css_unit(self):
        invalid_items = [
            '',
            '.',
            'asd',
            '3',
            '3km',
            '3.%',
            '3$',
            '00',
        ]
        self.invalid_check(invalid_items)
        print('OK - test_invalid_css_unit')
