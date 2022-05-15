import unittest

from pyvalidator.is_BIC import is_bic
from . import print_test_ok


class TestIsBic(unittest.TestCase):

    def test_valid_bic_codes(self):
        for i in [
            'SBICKEN1345',
            'SBICKEN1',
            'SBICKENY',
            'SBICKEN1YYP',
        ]:
            self.assertTrue(is_bic(i))
        print_test_ok()

    def test_invalid_bic_codes(self):
        for i in [
            'SBIC23NXXX',
            'S23CKENXXXX',
            'SBICKENXX',
            'SBICKENXX9',
            'SBICKEN13458',
            'SBICKEN',
        ]:
            self.assertFalse(is_bic(i))
        print_test_ok()
