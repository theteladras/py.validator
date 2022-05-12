import unittest

from pyvalidator.is_ean import is_ean
from . import print_test_ok


class TestIsEan(unittest.TestCase):

    def test_valid_ean(self):
        for i in [
            '9421023610112',
            '1234567890128',
            '4012345678901',
            '9771234567003',
            '9783161484100',
            '73513537',
            '00012345600012',
            '10012345678902',
            '20012345678909',
        ]:
            self.assertTrue(is_ean(i))
        print_test_ok()

    def test_invalid_ean(self):
        for i in [
            '5901234123451',
            '079777681629',
            '0705632085948',
        ]:
            self.assertFalse(is_ean(i))
        print_test_ok()
