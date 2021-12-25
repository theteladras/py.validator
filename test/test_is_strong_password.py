import unittest
from pyvalidator import *

class TestIsStrongPassword(unittest.TestCase):
    options = {
        "min_length": 8,
        "min_lowercase": 1,
        "min_uppercase": 1,
        "min_numbers": 1,
        "min_symbols": 1,
    }

    def test_valid_stong_password(self):
        self.assertTrue(is_strong_password('%2%k{7BsL"M%Kd6e', self.options))
        self.assertTrue(is_strong_password('EXAMPLE of very long_password123!', self.options))
        self.assertTrue(is_strong_password('mxH_+2vs&54_+H3P', self.options))
        self.assertTrue(is_strong_password('+&DxJ=X7-4L8jRCD', self.options))
        self.assertTrue(is_strong_password('etV*p%Nr6w&H%FeF', self.options))
        print('OK - test_valid_stong_password')

    def test_invalid_stong_password(self):
        self.assertFalse(is_strong_password('', self.options))
        self.assertFalse(is_strong_password('password', self.options))
        self.assertFalse(is_strong_password('hunter2', self.options))
        self.assertFalse(is_strong_password('hello world', self.options))
        self.assertFalse(is_strong_password('passw0rd', self.options))
        self.assertFalse(is_strong_password('password!', self.options))
        self.assertFalse(is_strong_password('PASSWORD!', self.options))
        print('OK - test_invalid_stong_password')
