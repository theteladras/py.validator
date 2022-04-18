import unittest

from pyvalidator import *


class TestIsMacAddress(unittest.TestCase):
	def valid_check(self, items, options = {}):
		for item in items:
			try:
				self.assertTrue(is_mac_address(item, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items, options = {}):
		for item in items:
			try:
				self.assertFalse(is_mac_address(item, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_mac_address(self):
		valid = [
			'ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:ab',
			'01:AB:03:04:05:06',
			'A9 C5 D4 9F EB D3',
			'01 02 03 04 05 ab',
			'01-02-03-04-05-ab',
			'0102.0304.05ab',
			'ab:ab:ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:06:07:ab',
			'01:AB:03:04:05:06:07:08',
			'A9 C5 D4 9F EB D3 B6 65',
			'01 02 03 04 05 06 07 ab',
			'01-02-03-04-05-06-07-ab',
			'0102.0304.0506.07ab',
        ]

		self.valid_check(valid)
		print('OK - test_valid_mac_address')

	def test_invalid_mac_address(self):
		invalid = [
			' ',
			'0:0:0:0',
			' : ',
			'abc',
			'01:02:03:04:05',
			'01:02:03:04:05:z0',
			'01:02:03:04::ab',
			'1:2:3:4:5:6',
			'AB:CD:EF:GH:01:02',
			'A9C5 D4 9F EB D3',
			'01-02 03:04 05 ab',
			'0102.03:04.05ab',
			'900f/dffs/sdea',
			'01:02:03:04:05:06:07',
			'01:02:03:04:05:06:07:z0',
			'01:02:03:04:05:06::ab',
			'1:2:3:4:5:6:7:8',
			'AB:CD:EF:GH:01:02:03:04',
			'A9C5 D4 9F EB D3 B6 65',
			'01-02 03:04 05 06 07 ab',
			'0102.03:04.0506.07ab',
			'900f/dffs/sdea/54gh',
        ]
		self.invalid_check(invalid)
		print('OK - test_invalid_mac_address')

	def test_valid_mac_address_eui48(self):
		valid = [
			'ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:ab',
			'01:AB:03:04:05:06',
			'A9 C5 D4 9F EB D3',
			'01 02 03 04 05 ab',
			'01-02-03-04-05-ab',
			'0102.0304.05ab',
        ]

		self.valid_check(valid, { "eui": 48 })
		print('OK - test_valid_mac_address_eui48')

	def test_invalid_mac_address_eui48(self):
		invalid = [
			'ab:ab:ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:06:07:ab',
			'01:AB:03:04:05:06:07:08',
			'A9 C5 D4 9F EB D3 B6 65',
			'01 02 03 04 05 06 07 ab',
			'01-02-03-04-05-06-07-ab',
			'0102.0304.0506.07ab',
        ]
		self.invalid_check(invalid, { "eui": 48 })
		print('OK - test_invalid_mac_address_eui48')

	def test_valid_mac_address_eui64(self):
		valid = [
			'ab:ab:ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:06:07:ab',
			'01:AB:03:04:05:06:07:08',
			'A9 C5 D4 9F EB D3 B6 65',
			'01 02 03 04 05 06 07 ab',
			'01-02-03-04-05-06-07-ab',
			'0102.0304.0506.07ab',
        ]

		self.valid_check(valid, { "eui": 64 })
		print('OK - test_valid_mac_address_eui64')

	def test_invalid_mac_address_eui64(self):
		invalid = [
			'ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:ab',
			'01:AB:03:04:05:06',
			'A9 C5 D4 9F EB D3',
			'01 02 03 04 05 ab',
			'01-02-03-04-05-ab',
			'0102.0304.05ab',
        ]
		self.invalid_check(invalid, { "eui": 64 })
		print('OK - test_invalid_mac_address_eui64')

	def test_valid_mac_address_no_separator(self):
		valid = [
			'abababababab',
        	'FFFFFFFFFFFF',
			'0102030405ab',
			'01AB03040506',
			'abababababababab',
			'FFFFFFFFFFFFFFFF',
			'01020304050607ab',
			'01AB030405060708',
        ]

		self.valid_check(valid, { "no_separators": True })
		print('OK - test_valid_mac_address_no_separator')

	def test_invalid_mac_address_no_separators(self):
		invalid = [
			'abc',
			'01:02:03:04:05',
			'01:02:03:04::ab',
			'1:2:3:4:5:6',
			'AB:CD:EF:GH:01:02',
			'ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:ab',
			'01:AB:03:04:05:06',
			'0102030405',
			'01020304ab',
			'123456',
			'ABCDEFGH0102',
			'01:02:03:04:05:06:07',
			'01:02:03:04:05:06::ab',
			'1:2:3:4:5:6:7:8',
			'AB:CD:EF:GH:01:02:03:04',
			'ab:ab:ab:ab:ab:ab:ab:ab',
			'FF:FF:FF:FF:FF:FF:FF:FF',
			'01:02:03:04:05:06:07:ab',
			'01:AB:03:04:05:06:07:08',
			'01020304050607',
			'010203040506ab',
			'12345678',
			'ABCDEFGH01020304',
        ]
		self.invalid_check(invalid, { "no_separators": True })
		print('OK - test_invalid_mac_address_no_separators')

	def test_valid_mac_address_no_separator_eui48(self):
		valid = [
			'abababababab',
			'FFFFFFFFFFFF',
			'0102030405ab',
			'01AB03040506',
        ]

		self.valid_check(valid, { "no_separators": True, "eui": 48 })
		print('OK - test_valid_mac_address_no_separator_eui48')

	def test_invalid_mac_address_no_separators_eui48(self):
		invalid = [
			'abababababababab',
			'FFFFFFFFFFFFFFFF',
			'01020304050607ab',
			'01AB030405060708',
        ]
		self.invalid_check(invalid, { "no_separators": True, "eui": 48 })
		print('OK - test_invalid_mac_address_no_separators_eui48')

	def test_valid_mac_address_no_separator_eui64(self):
		valid = [
			'abababababababab',
			'FFFFFFFFFFFFFFFF',
			'01020304050607ab',
			'01AB030405060708',
        ]

		self.valid_check(valid, { "no_separators": True, "eui": 64 })
		print('OK - test_valid_mac_address_no_separator_eui64')

	def test_invalid_mac_address_no_separators_eui64(self):
		invalid = [
			'abababababab',
			'FFFFFFFFFFFF',
			'0102030405ab',
			'01AB03040506',
        ]
		self.invalid_check(invalid, { "no_separators": True, "eui": 64 })
		print('OK - test_invalid_mac_address_no_separators_eui64')
