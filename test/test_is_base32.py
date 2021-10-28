import unittest
import validator

class TestIsBase32(unittest.TestCase):

    def test_valid_base32(self):
        self.assertTrue(validator.is_base32('ZG======'))
        self.assertTrue(validator.is_base32('JBSQ===='))
        self.assertTrue(validator.is_base32('JBSWY==='))
        self.assertTrue(validator.is_base32('K5SWYY3PNVSSA5DPEBXG6ZA='))
        self.assertTrue(validator.is_base32('K5SWYY3PNVSSA5DPEBXG6==='))
        print('OK - test_valid_base32')

    def test_invalid_base32(self):
        self.assertFalse(validator.is_base32('12345'))
        self.assertFalse(validator.is_base32(''))
        self.assertFalse(validator.is_base32('ZG====='))
        self.assertFalse(validator.is_base32('Zm=8JBSWY3DP'))
        self.assertFalse(validator.is_base32('=m9vYg=='))
        self.assertFalse(validator.is_base32('Zm9vYm/y===='))
        print('OK - test_invalid_base32')
