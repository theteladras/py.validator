import unittest
from validator import *

class TestIsBoolean(unittest.TestCase):

    def test_valid_booleans(self):
        self.assertTrue(is_boolean('True'))
        self.assertTrue(is_boolean('False'))
        self.assertTrue(is_boolean('true'))
        self.assertTrue(is_boolean('false'))
        self.assertTrue(is_boolean('0'))
        self.assertTrue(is_boolean('1'))
        print('OK - test_valid_booleans')

    def test_invalid_booleans(self):
        self.assertFalse(is_boolean('1.0'))
        self.assertFalse(is_boolean('0.0'))
        self.assertFalse(is_boolean('true '))
        self.assertFalse(is_boolean('yes'))
        print('OK - test_invalid_booleans')

    def test_valid_loosly_booleans(self):
        self.assertTrue(is_boolean('true', { "loose": True }))
        self.assertTrue(is_boolean('True', { "loose": True }))
        self.assertTrue(is_boolean('TRUE', { "loose": True }))
        self.assertTrue(is_boolean('false', { "loose": True }))
        self.assertTrue(is_boolean('False', { "loose": True }))
        self.assertTrue(is_boolean('FALSE', { "loose": True }))
        self.assertTrue(is_boolean('0', { "loose": True }))
        self.assertTrue(is_boolean('1', { "loose": True }))
        self.assertTrue(is_boolean('yes', { "loose": True }))
        self.assertTrue(is_boolean('Yes', { "loose": True }))
        self.assertTrue(is_boolean('YES', { "loose": True }))
        self.assertTrue(is_boolean('no', { "loose": True }))
        self.assertTrue(is_boolean('No', { "loose": True }))
        self.assertTrue(is_boolean('NO', { "loose": True }))
        print('OK - test_valid_loosly_booleans')

    def test_invalid_loosly_booleans(self):
        self.assertFalse(is_boolean('1.0', { "loose": True }))
        self.assertFalse(is_boolean('0.0', { "loose": True }))
        self.assertFalse(is_boolean('true ', { "loose": True }))
        self.assertFalse(is_boolean(' false', { "loose": True }))
        print('OK - test_invalid_loosly_booleans')
