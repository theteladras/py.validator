import unittest

from pyvalidator.is_base64 import is_base64
from . import print_test_ok


class TestIsBase58(unittest.TestCase):

    def test_valid_base64(self):
        for i in [
            '',
            'Zg==',
            'Zm8=',
            'Zm9v',
            'Zm9vYg==',
            'Zm9vYmE=',
            'Zm9vYmFy',
            'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4=',
            'Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg==',
            'U3VzcGVuZGlzc2UgbGVjdHVzIGxlbw==',
            'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuMPNS1Ufof9EW/M98FNw',
            'UAKrwflsqVxaxQjBQnHQmiI7Vac40t8x7pIb8gLGV6wL7sBTJiPovJ0V7y7oc0Ye',
            'rhKh0Rm4skP2z/jHwwZICgGzBvA0rH8xlhUiTvcwDCJ0kc+fh35hNt8srZQM4619',
            'FTgB66Xmp4EtVyhpQV+t02g6NzK72oZI0vnAvqhpkxLeLiMCyrI416wHm5Tkukhx',
            'QmcL2a6hNOyu0ixX/x2kSFXApEnVrJ+/IxGyfyw8kf4N2IZpW5nEP847lpfj0SZZ',
            'Fwrd1mnfnDbYohX2zRptLy2ZUn06Qo9pkG5ntvFEPo9bfZeULtjYzIl6K8gJ2uGZ',
            'HQIDAQAB',
        ]:
            self.assertTrue(is_base64(i))
        print_test_ok()

    def test_invalid_base64(self):
        for i in [
            '12345',
            'Vml2YW11cyBmZXJtZtesting123',
            'Zg=',
            'Z===',
            'Zm=8',
            '=m9vYg==',
            'Zm9vYmFy====',
        ]:
            self.assertFalse(is_base64(i))
        print_test_ok()

    def test_valid_base64_with_url_safe_flag(self):
        for i in [
            '',
            'bGFkaWVzIGFuZCBnZW50bGVtZW4sIHdlIGFyZSBmbG9hdGluZyBpbiBzcGFjZQ',
            '1234',
            'bXVtLW5ldmVyLXByb3Vk',
            'PDw_Pz8-Pg',
            'VGhpcyBpcyBhbiBlbmNvZGVkIHN0cmluZw',
        ]:
            self.assertTrue(is_base64(i, {'url_safe': True}))
        print_test_ok()

    def test_invalid_base64_with_url_safe_flag(self):
        for i in [
            ' AA',
            '\tAA',
            '\rAA',
            '\nAA',
            'This+isa/bad+base64Url==',
            '0K3RgtC+INC30LDQutC+0LTQuNGA0L7QstCw0L3QvdCw0Y8g0YHRgtGA0L7QutCw',
        ]:
            self.assertFalse(is_base64(i, {'url_safe': True}))
        print_test_ok()
