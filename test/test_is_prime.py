import unittest

from pyvalidator import *


class TestIsPrime(unittest.TestCase):
	def valid_check(self, items):
		for item in items:
			try:
				self.assertTrue(is_prime(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items):
		for item in items:
			try:
				self.assertFalse(is_prime(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_prime(self):
		valid_items = [
			'2',
			'3',
			'5',
			'7',
			'11',
			'13',
			'17',
			'19',
			'23',
			'29',
			'31',
			2,
			3,
			5,
			7,
			11,
			13,
			17,
			19,
			23,
			29,
			31,
			37,
			41,
			43,
			47,
			53,
			59,
			61,
			67,
			71,
			73,
			79,
			83,
			89,
			97,
			21577
        ]
		self.valid_check(valid_items)
		print('OK - test_valid_prime')

	def test_invalid_prime(self):
		invalid_items = [
			1,
			4,
			6,
			8,
			9,
			10,
			12,
			14,
			15,
			16,
			18,
			20,
			21,
			22,
			24,
			25,
			26,
			27,
			28,
			30,
			32,
			33,
			34,
			35,
			36,
			38,
			39,
			40,
			42,
			44,
			45,
			46,
			48,
			49,
			50,
			51,
			52,
			54,
			55,
			56,
			57,
			58,
			60,
			62,
			63,
			'51',
			'52',
			'54',
			'55',
			'56',
			'57',
			'58',
			'60',
			'62',
			'63',
        ]
		self.invalid_check(invalid_items)
		print('OK - test_invalid_prime')
