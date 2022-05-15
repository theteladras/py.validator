import unittest

from pyvalidator.is_strong_password import is_strong_password
from . import print_test_ok


class TestIsStrongPassword(unittest.TestCase):
    options = {
        "min_length": 8,
        "min_lowercase": 1,
        "min_uppercase": 1,
        "min_numbers": 1,
        "min_symbols": 1,
    }

    def test_valid_stong_password(self):
        for i in [
            '%2%k{7BsL"M%Kd6e',
            'EXAMPLE of very long_password123!',
            'mxH_+2vs&54_+H3P',
            '+&DxJ=X7-4L8jRCD',
            'etV*p%Nr6w&H%FeF',
        ]:
            self.assertTrue(is_strong_password(i, self.options))
        print_test_ok()

    def test_invalid_stong_password(self):
        for i in [
            '',
            'password',
            'hunter2',
            'hello world',
            'passw0rd',
            'password!',
            'PASSWORD!',
        ]:
            self.assertFalse(is_strong_password(i, self.options))
        print_test_ok()
