import unittest
from pyvalidator import *

class TestIsEthereumAddress(unittest.TestCase):

    def test_valid_ethereum_address(self):
        self.assertTrue(is_ethereum_address('0x0000000000000000000000000000000000000001'))
        self.assertTrue(is_ethereum_address('0x683E07492fBDfDA84457C16546ac3f433BFaa128'))
        self.assertTrue(is_ethereum_address('0x88dA6B6a8D3590e88E0FcadD5CEC56A7C9478319'))
        self.assertTrue(is_ethereum_address('0x8a718a84ee7B1621E63E680371e0C03C417cCaF6'))
        self.assertTrue(is_ethereum_address('0xFCb5AFB808b5679b4911230Aa41FfCD0cd335b42'))
        print('OK - test_valid_ethereum_address')

    def test_invalid_ethereum_address(self):
        self.assertFalse(is_ethereum_address('0xGHIJK05pwm37asdf5555QWERZCXV2345AoEuIdHt'))
        self.assertFalse(is_ethereum_address('0xFCb5AFB808b5679b4911230Aa41FfCD0cd335b422222'))
        self.assertFalse(is_ethereum_address('0xFCb5AFB808b5679b4911230Aa41FfCD0cd33'))
        self.assertFalse(is_ethereum_address('0b0110100001100101011011000110110001101111'))
        self.assertFalse(is_ethereum_address('683E07492fBDfDA84457C16546ac3f433BFaa128'))
        self.assertFalse(is_ethereum_address('1C6o5CDkLxjsVpnLSuqRs1UBFozXLEwYvU'))
        print('OK - test_invalid_ethereum_address')
