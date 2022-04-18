import unittest
import warnings

from pyvalidator import *


class TestIsOnline(unittest.TestCase):
	def valid_check(self, items = None):
		for item in items:
			try:
				self.assertTrue(is_online(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items = None):
		for item in items:
			try:
				self.assertFalse(is_online(item))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_is_online(self):
		try:
			self.valid_check([None]) # NOTE if internet connection on the machine is not available this test might fail
		except:
			warnings.warn('this test is expected to fail if the internet connection is not available')

	def test_reachable_urls(self):
		valid_items = [
			'google.com',
			'yahoo.com',
			'https://linkedin.com',
			'http://stackoverflow.com/'
        ]
		try:
			self.valid_check(valid_items)
			print('OK - test_reachable_urls')
		except:
			warnings.warn('This means that either the machine is offline or the testing urls are down, in which case the tesst fail is expected')

	def test_unreachable_url(self):
		invalid_items = [
			' ',
			'thisshouldneverexist.no.way.com',
			'asd'
        ]
		self.invalid_check(invalid_items)
		print('OK - test_unreachable_url')
