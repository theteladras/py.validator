import unittest
from pyvalidator import *

class TestIsFqdn(unittest.TestCase):

    def test_valid_fqdn(self):
        self.assertTrue(is_fqdn('domain.com'))
        self.assertTrue(is_fqdn('dom.plato'))
        self.assertTrue(is_fqdn('a.domain.co'))
        self.assertTrue(is_fqdn('foo--bar.com'))
        self.assertTrue(is_fqdn('xn--froschgrn-x9a.com'))
        self.assertTrue(is_fqdn('rebecca.blackfriday'))
        self.assertTrue(is_fqdn('1337.com'))
        print('OK - test_valid_fqdn')

    def test_invalid_fqdn(self):
        self.assertFalse(is_fqdn('abc'))
        self.assertFalse(is_fqdn('256.0.0.0'))
        self.assertFalse(is_fqdn('_.com'))
        self.assertFalse(is_fqdn('*.some.com'))
        self.assertFalse(is_fqdn('s!ome.com'))
        self.assertFalse(is_fqdn('domain.com/'))
        self.assertFalse(is_fqdn('/more.com'))
        self.assertFalse(is_fqdn('domain.com�'))
        self.assertFalse(is_fqdn('domain.co\u00A0m'))
        self.assertFalse(is_fqdn('domain.co\u1680m'))
        self.assertFalse(is_fqdn('domain.co\u2006m'))
        self.assertFalse(is_fqdn('domain.co\u2028m'))
        self.assertFalse(is_fqdn('domain.co\u2029m'))
        self.assertFalse(is_fqdn('domain.co\u202Fm'))
        self.assertFalse(is_fqdn('domain.co\u205Fm'))
        self.assertFalse(is_fqdn('domain.co\u3000m'))
        self.assertFalse(is_fqdn('domain.com\uDC00'))
        self.assertFalse(is_fqdn('domain.co\uEFFFm'))
        self.assertFalse(is_fqdn('domain.co\uFDDAm'))
        self.assertFalse(is_fqdn('domain.co\uFFF4m'))
        self.assertFalse(is_fqdn('domain.com©'))
        self.assertFalse(is_fqdn('example.0'))
        self.assertFalse(is_fqdn('192.168.0.9999'))
        self.assertFalse(is_fqdn('192.168.0'))
        print('OK - test_invalid_fqdn')

    def test_valid_fqdn_with_trailing_dot(self):
        self.assertTrue(is_fqdn('domain.com.', { "allow_trailing_dot": True }))
        print('OK - test_valid_fqdn_with_trailing_dot')

    def test_invalid_fqdn_with_not_required_tld(self):
        self.assertFalse(is_fqdn('example.0', { "require_tld": False }))
        self.assertFalse(is_fqdn('192.168.0', { "require_tld": False }))
        self.assertFalse(is_fqdn('192.168.0.9999', { "require_tld": False }))
        print('OK - test_invalid_fqdn_with_not_required_tld')

    def test_valid_fqdn_with_allowed_wildcard(self):
        self.assertTrue(is_fqdn('*.domain.com', { "allow_wildcard": True }))
        self.assertTrue(is_fqdn('*.global.domain.com', { "allow_wildcard": True }))
        print('OK - test_valid_fqdn_with_allowed_wildcard')

    def test_valid_fqdn_with_not_required_tld_but_allowed_numeric_tld(self):
        self.assertTrue(is_fqdn('example.0', { "require_tld": False, "allow_numeric_tld": True }))
        self.assertTrue(is_fqdn('192.168.0', { "require_tld": False, "allow_numeric_tld": True }))
        self.assertTrue(is_fqdn('192.168.0.9999', { "require_tld": False, "allow_numeric_tld": True }))
        print('OK - test_valid_fqdn_with_not_required_tld_but_allowed_numeric_tld')
