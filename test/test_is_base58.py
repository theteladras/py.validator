import unittest
import validator

class TestIsBase58(unittest.TestCase):

    def test_valid_base58(self):
        self.assertTrue(validator.is_base58('BukQL'))
        self.assertTrue(validator.is_base58('3KMUV89zab'))
        self.assertTrue(validator.is_base58('91GHkLMNtyo98'))
        self.assertTrue(validator.is_base58('YyjKm3H'))
        self.assertTrue(validator.is_base58('Mkhss145TRFg'))
        self.assertTrue(validator.is_base58('7678765677'))
        self.assertTrue(validator.is_base58('abcodpq'))
        self.assertTrue(validator.is_base58('AAVHJKLPY'))
        print('OK - test_valid_base58')

    def test_invalid_base58(self):
        self.assertFalse(validator.is_base58('0OPLJH'))
        self.assertFalse(validator.is_base58('IMKLP23'))
        self.assertFalse(validator.is_base58('KLMOmk986'))
        self.assertFalse(validator.is_base58('LL1l1985hG'))
        self.assertFalse(validator.is_base58('*MP9K'))
        self.assertFalse(validator.is_base58(')()(=9292929MKL'))
        print('OK - test_invalid_base58')
