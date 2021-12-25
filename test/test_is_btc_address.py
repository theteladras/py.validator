import unittest
from pyvalidator import *

class TestIsBtcAddress(unittest.TestCase):

    def test_valid_btc_address(self):
        self.assertTrue(is_btc_address('1MUz4VMYui5qY1mxUiG8BQ1Luv6tqkvaiL'))
        self.assertTrue(is_btc_address('3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy'))
        self.assertTrue(is_btc_address('bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq'))
        self.assertTrue(is_btc_address('14qViLJfdGaP4EeHnDyJbEGQysnCpwk3gd'))
        self.assertTrue(is_btc_address('35bSzXvRKLpHsHMrzb82f617cV4Srnt7hS'))
        self.assertTrue(is_btc_address('17VZNX1SN5NtKa8UQFxwQbFeFc3iqRYhemt'))
        self.assertTrue(is_btc_address('bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4'))
        print('OK - test_valid_btc_address')

    def test_invalid_btc_address(self):
        self.assertFalse(is_btc_address('4J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy'))
        self.assertFalse(is_btc_address('0x56F0B8A998425c53c75C4A303D4eF987533c5597'))
        self.assertFalse(is_btc_address('pp8skudq3x5hzw8ew7vzsw8tn4k8wxsqsv0lt0mf3g'))
        self.assertFalse(is_btc_address('17VZNX1SN5NlKa8UQFxwQbFeFc3iqRYhem'))
        self.assertFalse(is_btc_address('BC1QW508D6QEJXTDG4Y5R3ZARVAYR0C5XW7KV8F3T4'))
        print('OK - test_invalid_btc_address')
