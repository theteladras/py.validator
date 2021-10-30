import unittest
import validator

class TestIsBIC(unittest.TestCase):

    def test_valid_bic_codes(self):
        self.assertTrue(validator.is_bic('SBICKEN1345'))
        self.assertTrue(validator.is_bic('SBICKEN1'))
        self.assertTrue(validator.is_bic('SBICKENY'))
        self.assertTrue(validator.is_bic('SBICKEN1YYP'))
        print('OK - test_valid_bic_codes')

    def test_invalid_bic_codes(self):
        self.assertFalse(validator.is_bic('SBIC23NXXX'))
        self.assertFalse(validator.is_bic('S23CKENXXXX'))
        self.assertFalse(validator.is_bic('SBICKENXX'))
        self.assertFalse(validator.is_bic('SBICKENXX9'))
        self.assertFalse(validator.is_bic('SBICKEN13458'))
        self.assertFalse(validator.is_bic('SBICKEN'))
        print('OK - test_invalid_bic_codes')
