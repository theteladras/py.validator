import unittest

from pyvalidator import *


class TestIsOdd(unittest.TestCase):
	def valid_check(self, items):
		for item in items:
			try:
				self.assertTrue(is_odd(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items):
		for item in items:
			try:
				self.assertFalse(is_odd(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_odd(self):
		valid_items = [
			1,
			3,
			5,
			7,
			9,
			111,
			2019,
			-1
        ]
		self.valid_check(valid_items)
		print('OK - test_valid_odd')

	def test_invalid_odd(self):
		invalid_items = [
			' ',
			'a',
			'.1',
			'1.1',
			0,
			2,
			110,
			220,
			2020,
			'2020',
			'666',
			'2',
			'0'
        ]
		self.invalid_check(invalid_items)
		print('OK - test_invalid_odd')
