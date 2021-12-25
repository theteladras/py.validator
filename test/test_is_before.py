import unittest
from pyvalidator import *
import datetime

class TestIsBefore(unittest.TestCase):

    def test_valid_before_dates_against_a_start_date(self):
        self.assertTrue(is_before('2010-07-02', '08/04/2011'))
        self.assertTrue(is_before('2010-08-04', '08/04/2011'))
        self.assertTrue(is_before(datetime.datetime.utcfromtimestamp(0).isoformat(), '08/04/2011'))
        print('OK - test_valid_before_dates_against_a_start_date')

    def test_invalid_before_dates_against_a_start_date(self):
        self.assertFalse(is_before('08/04/2011', '08/04/2011'))
        self.assertFalse(is_before(datetime.datetime(2011, 9, 10).isoformat(), '08/04/2011'))
        print('OK - test_invalid_before_dates_against_a_start_date')
