import unittest
from validator import *

class TestIsMd5(unittest.TestCase):

    def test_valid_md5(self):
        self.assertTrue(is_md5('d94f3f016ae679c3008de268209132f0'))
        self.assertTrue(is_md5('751adbc511ccbe8edf23d486fa4581c0'))
        self.assertTrue(is_md5('88dae00e614d8f24cfd5a8b3f8002e99'))
        self.assertTrue(is_md5('0bf1c35032a71a14c2f719e5a14c1e99'))
        print('OK - test_valid_md5')

    def test_invalid_md5(self):
        self.assertFalse(is_md5('KYT0bf1c35032a71a14c2f719e5a14c1'))
        self.assertFalse(is_md5('q94375dj93458w31'))
        self.assertFalse(is_md5('39485729341'))
        self.assertFalse(is_md5('%&FHKJFvc'))
        self.assertFalse(is_md5(''))
        print('OK - test_invalid_md5')

    def test_fail_md5(self):
        self.assertRaises(Exception, is_md5, None)
        self.assertRaises(Exception, is_md5, {})
