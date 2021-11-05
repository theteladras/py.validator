import unittest
from validator import *

class TestIsBic(unittest.TestCase):

    def test_valid_bic_codes(self):
        self.assertTrue(is_bic('SBICKEN1345'))
        self.assertTrue(is_bic('SBICKEN1'))
        self.assertTrue(is_bic('SBICKENY'))
        self.assertTrue(is_bic('SBICKEN1YYP'))
        print('OK - test_valid_bic_codes')

    def test_invalid_bic_codes(self):
        self.assertFalse(is_bic('SBIC23NXXX'))
        self.assertFalse(is_bic('S23CKENXXXX'))
        self.assertFalse(is_bic('SBICKENXX'))
        self.assertFalse(is_bic('SBICKENXX9'))
        self.assertFalse(is_bic('SBICKEN13458'))
        self.assertFalse(is_bic('SBICKEN'))
        print('OK - test_invalid_bic_codes')
