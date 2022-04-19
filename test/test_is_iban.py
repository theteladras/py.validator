import unittest

from pyvalidator import *


class TestIsIban(unittest.TestCase):

	def test_valid_odd(self):
		self.assertTrue(is_iban('AD12 0001 2030 2003 5910 0100'))
		self.assertTrue(is_iban('AD1200012030200359100100'))
		self.assertTrue(is_iban('DE89370400440532013000'))
		self.assertTrue(is_iban('HU42117730161111101800000000'))
		self.assertTrue(is_iban('FR14 2004 1010 0505 0001 3M02 606'))
		self.assertTrue(is_iban('ES9121000418450200051332'))
		self.assertTrue(is_iban('UA213223130000026007233566001'))
		self.assertTrue(is_iban('NO93 8601 1117 947'))
		self.assertTrue(is_iban('RS35 2600 0560 1001 6113 79'))
		self.assertTrue(is_iban('GB29 NWBK 6016 1331 9268 19'))
		print('OK - test_valid_odd')

	def test_invalid_odd(self):
		self.assertFalse(is_iban('AD12 0001 2030 2003 5910 01001'))
		self.assertFalse(is_iban('HU421177301611111018000000001'))
		self.assertFalse(is_iban('FR14 2004 1010 0505 000 3M02 606'))
		self.assertFalse(is_iban('ES912000418450200051332'))
		self.assertFalse(is_iban('UAA213223130000026007233566001'))
		self.assertFalse(is_iban('NO93 8601 117 947'))
		self.assertFalse(is_iban('RS35 063 0560 1001 6113 79'))
		self.assertFalse(is_iban('GB29 NWBKA 6016 1331 9268 19'))
		self.assertFalse(is_iban('GB29 NWB 6016 1331 9268 19'))
		print('OK - test_invalid_odd')
