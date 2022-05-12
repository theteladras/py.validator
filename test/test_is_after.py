import datetime
import unittest

from pyvalidator.is_after import is_after
from . import print_test_ok


class TestIsAfter(unittest.TestCase):

    def test_valid_after_dates_against_a_start_date(self):
        for i in [
            ['2011-08-04', '2011-08-03'],
            [datetime.datetime.now().isoformat(), '2011-08-03'],
        ]:
            self.assertTrue(is_after(*i))
        print_test_ok()

    def test_invalid_after_dates_against_a_start_date(self):
        for i in [
            ['2011-07-02', '2011-08-03'],
            ['2011-08-03', '2011-08-03'],
            [datetime.datetime.utcfromtimestamp(0).isoformat(), '2011-08-03'],
            ['foo', '2011-08-03'],
        ]:
            self.assertFalse(is_after(*i))
        print_test_ok()
