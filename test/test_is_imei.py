import unittest

from pyvalidator.is_imei import is_imei
from . import print_test_ok


class TestIsImei(unittest.TestCase):

    def test_valid_imei(self):
        for i in [
            '352099001761481',
            '868932036356090',
            '490154203237518',
            '546918475942169',
            '998227667144730',
            '532729766805999',
        ]:
            self.assertTrue(is_imei(i))
        print_test_ok()

    def test_invalid_imei(self):
        for i in [
            '490154203237517',
            '3568680000414120',
            '3520990017614823',
        ]:
            self.assertFalse(is_imei(i))
        print_test_ok()

    def test_valid_imei_with_hyphens(self):
        for i in [
            '35-209900-176148-1',
            '86-893203-635609-0',
            '49-015420-323751-8',
            '54-691847-594216-9',
            '99-822766-714473-0',
            '53-272976-680599-9',
        ]:
            self.assertTrue(is_imei(i, {"allow_hyphens": True}))
        print_test_ok()

    def test_invalid_imei_with_hyphens(self):
        for i in [
            '49-015420-323751-7',
            '35-686800-0041412-0',
            '35-209900-1761482-3',
            '3520990017614823',
        ]:
            self.assertFalse(is_imei(i, {"allow_hyphens": True}))
        print_test_ok()
