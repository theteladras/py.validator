import unittest
import validator

class TestIsIsrc(unittest.TestCase):

    def test_valid_isrc(self) -> bool:
        self.assertTrue(validator.is_isrc('USAT29900609'))
        self.assertTrue(validator.is_isrc('GBAYE6800011'))
        self.assertTrue(validator.is_isrc('USRC15705223'))
        self.assertTrue(validator.is_isrc('USCA29500702'))
        print('OK - test_valid_isrc')

    def test_invalid_isrc(self):
        self.assertFalse(validator.is_isrc('USAT2990060'))
        self.assertFalse(validator.is_isrc('SRC15705223'))
        self.assertFalse(validator.is_isrc('US-CA29500702'))
        self.assertFalse(validator.is_isrc('USARC15705223'))
        print('OK - test_invalid_isrc')

    def test_fail_isrc(self):
        self.assertRaises(Exception, validator.is_isrc)
