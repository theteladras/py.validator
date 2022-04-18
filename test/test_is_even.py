import unittest

from pyvalidator import *


class TestIsEven(unittest.TestCase):
	def valid_check(self, items):
		for item in items:
			try:
				self.assertTrue(is_even(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items):
		for item in items:
			try:
				self.assertFalse(is_even(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_even(self):
		valid_items = [
			0,
			2,
			4,
			6,
			8,
			10,
			12,
			120,
			1000,
			-1000,
			'1000',
			'2',
			'120',
			'666',
			'-888'
        ]
		self.valid_check(valid_items)
		print('OK - test_valid_even')

	def test_invalid_even(self):
		invalid_items = [
			' ',
			'a',
			'.1',
			'1.0',
			3,
			5,
			111,
			-7,
			'17',
			'-21',
			'121'
        ]
		self.invalid_check(invalid_items)
		print('OK - test_invalid_even')
