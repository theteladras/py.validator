import unittest

from pyvalidator.is_md5 import is_md5
from . import print_test_ok


class TestIsMd5(unittest.TestCase):

    def test_valid_md5(self):
        for i in [
            'd94f3f016ae679c3008de268209132f0',
            '751adbc511ccbe8edf23d486fa4581c0',
            '88dae00e614d8f24cfd5a8b3f8002e99',
            '0bf1c35032a71a14c2f719e5a14c1e99',
        ]:
            self.assertTrue(is_md5(i))
        print_test_ok()

    def test_invalid_md5(self):
        for i in [
            'KYT0bf1c35032a71a14c2f719e5a14c1',
            'q94375dj93458w31',
            '39485729341',
            '%&FHKJFvc',
            '',
        ]:
            self.assertFalse(is_md5(i))
        print_test_ok()

    def test_fail_md5(self):
        self.assertRaises(Exception, is_md5, None)
        self.assertRaises(Exception, is_md5, {})
        print_test_ok()
