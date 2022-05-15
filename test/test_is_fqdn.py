import unittest

from pyvalidator.is_fqdn import is_fqdn
from . import print_test_ok


class TestIsFqdn(unittest.TestCase):

    def test_valid_fqdn(self):
        for i in [
            'domain.com',
            'dom.plato',
            'a.domain.co',
            'foo--bar.com',
            'xn--froschgrn-x9a.com',
            'rebecca.blackfriday',
            '1337.com',
        ]:
            self.assertTrue(is_fqdn(i))
        print_test_ok()

    def test_invalid_fqdn(self):
        for i in [
            'abc',
            '256.0.0.0',
            '_.com',
            '*.some.com',
            's!ome.com',
            'domain.com/',
            '/more.com',
            'domain.com�',
            'domain.co\u00A0m',
            'domain.co\u1680m',
            'domain.co\u2006m',
            'domain.co\u2028m',
            'domain.co\u2029m',
            'domain.co\u202Fm',
            'domain.co\u205Fm',
            'domain.co\u3000m',
            'domain.com\uDC00',
            'domain.co\uEFFFm',
            'domain.co\uFDDAm',
            'domain.co\uFFF4m',
            'domain.com©',
            'example.0',
            '192.168.0.9999',
            '192.168.0',
        ]:
            self.assertFalse(is_fqdn(i))
        print_test_ok()

    def test_valid_fqdn_with_trailing_dot(self):
        for i in [
            'domain.com.',
        ]:
            self.assertTrue(is_fqdn(i, {"allow_trailing_dot": True}))
        print_test_ok()

    def test_invalid_fqdn_with_not_required_tld(self):
        for i in [
            'example.0',
            '192.168.0',
            '192.168.0.9999',
        ]:
            self.assertFalse(is_fqdn(i, {"require_tld": False}))
        print_test_ok()

    def test_valid_fqdn_with_allowed_wildcard(self):
        for i in [
            '*.domain.com',
            '*.global.domain.com',
        ]:
            self.assertTrue(is_fqdn(i, {"allow_wildcard": True}))
        print_test_ok()

    def test_valid_fqdn_with_not_required_tld_but_allowed_numeric_tld(self):
        for i in [
            'example.0',
            '192.168.0',
            '192.168.0.9999',
        ]:
            self.assertTrue(is_fqdn(i, {"require_tld": False, "allow_numeric_tld": True}))
        print_test_ok()
