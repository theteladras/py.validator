import datetime
import unittest

from pyvalidator.is_before import is_before
from . import print_test_ok


class TestIsBefore(unittest.TestCase):

    def test_valid_before_dates_against_a_start_date(self):
        for i in [
            ['2010-07-02', '08/04/2011'],
            ['2010-08-04', '08/04/2011'],
            [datetime.datetime.utcfromtimestamp(0).isoformat(), '08/04/2011'],
        ]:
            self.assertTrue(is_before(*i))
        print_test_ok()

    def test_invalid_before_dates_against_a_start_date(self):
        for i in [
            ['08/04/2011', '08/04/2011'],
            ['08/04/2011', '08/04/2011'],
            [datetime.datetime(2011, 9, 10).isoformat(), '08/04/2011'],
        ]:
            self.assertFalse(is_before(*i))
        print_test_ok()
