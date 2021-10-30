import unittest
import validator

class TestIsEan(unittest.TestCase):

    def test_valid_ean(self):
        self.assertTrue(validator.is_ean('9421023610112'))
        self.assertTrue(validator.is_ean('1234567890128'))
        self.assertTrue(validator.is_ean('4012345678901'))
        self.assertTrue(validator.is_ean('9771234567003'))
        self.assertTrue(validator.is_ean('9783161484100'))
        self.assertTrue(validator.is_ean('73513537'))
        self.assertTrue(validator.is_ean('00012345600012'))
        self.assertTrue(validator.is_ean('10012345678902'))
        self.assertTrue(validator.is_ean('20012345678909'))
        print('OK - test_valid_ean')

    def test_invalid_ean(self):
        self.assertFalse(validator.is_ean('5901234123451'))
        self.assertFalse(validator.is_ean('079777681629'))
        self.assertFalse(validator.is_ean('0705632085948'))
        print('OK - test_invalid_ean')