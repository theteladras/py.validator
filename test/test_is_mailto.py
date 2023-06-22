import unittest
from pyvalidator.is_mailto import is_valid_mailto_link
from . import print_test_ok

class TestIsValidMailtoLink(unittest.TestCase):
    
    def test_valid_mailto_link_with_single_email(self):
        link = "mailto:john@example.com"
        result = is_valid_mailto_link(link)
        self.assertTrue(result)
    
    def test_valid_mailto_link_with_multiple_emails(self):
        link = "mailto:john@example.com, jane@example.com, jake@example.com"
        result = is_valid_mailto_link(link)
        self.assertTrue(result)
    
    def test_invalid_mailto_link_missing_mailto_prefix(self):
        link = "john@example.com"
        result = is_valid_mailto_link(link)
        self.assertFalse(result)
    
    def test_invalid_mailto_link_missing_email(self):
        link = "mailto:"
        result = is_valid_mailto_link(link)
        self.assertFalse(result)
    
    def test_invalid_mailto_link_no_comma_separator(self):
        link = "mailto:john@example.com jane@example.com"
        result = is_valid_mailto_link(link)
        self.assertFalse(result)
    
    def test_invalid_mailto_link_invalid_email_format(self):
        link = "mailto:john@example.com, jane@example,com"
        result = is_valid_mailto_link(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_no_space_after_comma(self):
        link = "mailto:asd@asd.asd,asd@asd.de"
        result = is_valid_mailto_link(link)
        self.assertFalse(result)