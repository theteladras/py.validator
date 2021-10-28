import unittest
import validator
import datetime

class TestIsAfter(unittest.TestCase):

    def test_valid_after_dates_against_a_start_date(self):
        self.assertTrue(validator.is_after('2011-08-04', '2011-08-03'))
        self.assertTrue(validator.is_after(datetime.datetime.now().isoformat(), '2011-08-03'))
        print('OK - test_valid_after_dates_against_a_start_date')

    def test_invalid_after_dates_against_a_start_date(self):
        self.assertFalse(validator.is_after('2011-07-02', '2011-08-03'))
        self.assertFalse(validator.is_after('2011-08-03', '2011-08-03'))
        self.assertFalse(validator.is_after(datetime.datetime.utcfromtimestamp(0).isoformat(), '2011-08-03'))
        self.assertFalse(validator.is_after('foo', '2011-08-03'))
        print('OK - test_invalid_after_dates_against_a_start_date')
