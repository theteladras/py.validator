import unittest
from pyvalidator.is_mailto_uri import is_mailto_uri
from . import print_test_ok

class TestIsValidMailtoLink(unittest.TestCase):
    
    def test_valid_mailto_link_with_single_email(self):
        link = "mailto:john@example.com"
        result = is_mailto_uri(link)
        self.assertTrue(result)
    
    def test_valid_mailto_link_with_multiple_emails(self):
        link = "mailto:john@example.com,jane@example.com,jake@example.com"
        result = is_mailto_uri(link)
        self.assertTrue(result)
    
    def test_invalid_mailto_link_missing_mailto_prefix(self):
        link = "john@example.com"
        result = is_mailto_uri(link)
        self.assertFalse(result)
    
    def test_invalid_mailto_link_missing_email(self):
        link = "mailto:"
        result = is_mailto_uri(link)
        self.assertFalse(result)
    
    def test_invalid_mailto_link_no_comma_separator(self):
        link = "mailto:john@example.com jane@example.com"
        result = is_mailto_uri(link)
        self.assertFalse(result)
    
    def test_invalid_mailto_link_invalid_email_format(self):
        link = "mailto:john@example.com, jane@example,com"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_valid_mailto_link_for_multiple_emails(self):
        link = "mailto:asd@asd.asd,asd@asd.de"
        result = is_mailto_uri(link)
        self.assertTrue(result)

    def test_invalid_mailto_link_for_multiple_emails_with_no_space_between(self):
        link = "mailto:asd@asd.asd, asd@asd.de"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_contains_special_characters(self):
        link = "mailto:alice@example.com?subject=Meeting^Agenda"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_contains_incomplete_subject(self):
        link = "mailto:jane.smith@example.com?subject="
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_missing_monkey_char(self):
        link = "mailto:john.doeexample.com"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_missing_mailto(self):
        link = "john.doe@example.com"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_invalid_email(self):
        link = "mailto:invalid-email"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_incorect_parameter_name(self):
        link = "mailto:jane.smith@example.com?subj=Meeting%20Agenda"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_missing_email_address(self):
        link = "mailto:?subject=Feedback"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_invalid_mailto_link_unencoded_chars(self):
        link = "mailto:alice@example.com?subject=Meeting Agenda&body=Please%20bring*%20the%20documents"
        result = is_mailto_uri(link)
        self.assertFalse(result)

    def test_valid_mailto_link_for_multiple_emails_with_params(self):
        link = "mailto:alice@example.com,bob@example.com,carol@example.com?subject=Project%20Team"
        result = is_mailto_uri(link)
        self.assertTrue(result)

    def test_valid_mailto_link_with_cc_and_bcc(self):
        link = "mailto:support@example.com?cc=admin@example.com&bcc=manager@example.com"
        result = is_mailto_uri(link)
        self.assertTrue(result)

    def test_valid_mailto_link_with_cc(self):
        link = "mailto:support@example.com?cc=admin@example.com"
        result = is_mailto_uri(link)
        self.assertTrue(result)

    def test_valid_mailto_link_with_bcc(self):
        link = "mailto:support@example.com?bcc=admin@example.com"
        result = is_mailto_uri(link)
        self.assertTrue(result)

    def test_valid_mailto_link_with_bcc(self):
        link = "mailto:feedback@example.com?body=Dear%20Support,%0AI%20have%20a%20question%20about%20your%20product."
        result = is_mailto_uri(link)
        self.assertTrue(result)
