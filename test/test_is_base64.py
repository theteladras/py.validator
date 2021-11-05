import unittest
from validator import *

class TestIsBase58(unittest.TestCase):

    def test_valid_base64(self):
        self.assertTrue(is_base64(''))
        self.assertTrue(is_base64('Zg=='))
        self.assertTrue(is_base64('Zm8='))
        self.assertTrue(is_base64('Zm9v'))
        self.assertTrue(is_base64('Zm9vYg=='))
        self.assertTrue(is_base64('Zm9vYmE='))
        self.assertTrue(is_base64('Zm9vYmFy'))
        self.assertTrue(is_base64('TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(is_base64('Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(is_base64('U3VzcGVuZGlzc2UgbGVjdHVzIGxlbw=='))
        self.assertTrue(is_base64('MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuMPNS1Ufof9EW/M98FNw'))
        self.assertTrue(is_base64('UAKrwflsqVxaxQjBQnHQmiI7Vac40t8x7pIb8gLGV6wL7sBTJiPovJ0V7y7oc0Ye'))
        self.assertTrue(is_base64('rhKh0Rm4skP2z/jHwwZICgGzBvA0rH8xlhUiTvcwDCJ0kc+fh35hNt8srZQM4619'))
        self.assertTrue(is_base64('FTgB66Xmp4EtVyhpQV+t02g6NzK72oZI0vnAvqhpkxLeLiMCyrI416wHm5Tkukhx'))
        self.assertTrue(is_base64('QmcL2a6hNOyu0ixX/x2kSFXApEnVrJ+/IxGyfyw8kf4N2IZpW5nEP847lpfj0SZZ'))
        self.assertTrue(is_base64('Fwrd1mnfnDbYohX2zRptLy2ZUn06Qo9pkG5ntvFEPo9bfZeULtjYzIl6K8gJ2uGZ'))
        self.assertTrue(is_base64('HQIDAQAB'))
        print('OK - test_valid_base64')

    def test_invalid_base64(self):
        self.assertFalse(is_base64('12345'))
        self.assertFalse(is_base64('Vml2YW11cyBmZXJtZtesting123'))
        self.assertFalse(is_base64('Zg='))
        self.assertFalse(is_base64('Z==='))
        self.assertFalse(is_base64('Zm=8'))
        self.assertFalse(is_base64('=m9vYg=='))
        self.assertFalse(is_base64('Zm9vYmFy===='))
        print('OK - test_invalid_base64')

    def test_valid_base64_with_url_safe_flag(self):
        self.assertTrue(is_base64('', { 'url_safe': True }))
        self.assertTrue(is_base64('bGFkaWVzIGFuZCBnZW50bGVtZW4sIHdlIGFyZSBmbG9hdGluZyBpbiBzcGFjZQ', { 'url_safe': True }))
        self.assertTrue(is_base64('1234', { 'url_safe': True }))
        self.assertTrue(is_base64('bXVtLW5ldmVyLXByb3Vk', { 'url_safe': True }))
        self.assertTrue(is_base64('PDw_Pz8-Pg', { 'url_safe': True }))
        self.assertTrue(is_base64('VGhpcyBpcyBhbiBlbmNvZGVkIHN0cmluZw', { 'url_safe': True }))
        print('OK - test_valid_base64_with_url_safe_flag')

    def test_invalid_base64_with_url_safe_flag(self):
        self.assertFalse(is_base64(' AA', { 'url_safe': True }))
        self.assertFalse(is_base64('\tAA', { 'url_safe': True }))
        self.assertFalse(is_base64('\rAA', { 'url_safe': True }))
        self.assertFalse(is_base64('\nAA', { 'url_safe': True }))
        self.assertFalse(is_base64('This+isa/bad+base64Url==', { 'url_safe': True }))
        self.assertFalse(is_base64('0K3RgtC+INC30LDQutC+0LTQuNGA0L7QstCw0L3QvdCw0Y8g0YHRgtGA0L7QutCw', { 'url_safe': True }))
        print('OK - test_invalid_base64_with_url_safe_flag')
