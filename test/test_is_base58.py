import unittest

from pyvalidator.is_base58 import is_base58
from . import print_test_ok


class TestIsBase58(unittest.TestCase):

    def test_valid_base58(self):
        for i in [
            'BukQL',
            '3KMUV89zab',
            '91GHkLMNtyo98',
            'YyjKm3H',
            'Mkhss145TRFg',
            '7678765677',
            'abcodpq',
            'AAVHJKLPY',
        ]:
            self.assertTrue(is_base58(i))
        print_test_ok()

    def test_invalid_base58(self):
        for i in [
            '0OPLJH',
            'IMKLP23',
            'KLMOmk986',
            'LL1l1985hG',
            '*MP9K',
            ')()(=9292929MKL',
        ]:
            self.assertFalse(is_base58(i))
        print_test_ok()
