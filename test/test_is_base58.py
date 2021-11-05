import unittest
from validator import *

class TestIsBase58(unittest.TestCase):

    def test_valid_base58(self):
        self.assertTrue(is_base58('BukQL'))
        self.assertTrue(is_base58('3KMUV89zab'))
        self.assertTrue(is_base58('91GHkLMNtyo98'))
        self.assertTrue(is_base58('YyjKm3H'))
        self.assertTrue(is_base58('Mkhss145TRFg'))
        self.assertTrue(is_base58('7678765677'))
        self.assertTrue(is_base58('abcodpq'))
        self.assertTrue(is_base58('AAVHJKLPY'))
        print('OK - test_valid_base58')

    def test_invalid_base58(self):
        self.assertFalse(is_base58('0OPLJH'))
        self.assertFalse(is_base58('IMKLP23'))
        self.assertFalse(is_base58('KLMOmk986'))
        self.assertFalse(is_base58('LL1l1985hG'))
        self.assertFalse(is_base58('*MP9K'))
        self.assertFalse(is_base58(')()(=9292929MKL'))
        print('OK - test_invalid_base58')
