import unittest

from pyvalidator import *


class TestIsPalindrome(unittest.TestCase):
	def valid_check(self, items, options = {}):
		for item in items:
			try:
				self.assertTrue(is_palindrome(item, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items, options = {}):
		for item in items:
			try:
				self.assertFalse(is_palindrome(item, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_palindrome(self):
		valid_items = [
			'',
			'A',
			'EVE',
			'radar',
			'reviver',
			'top spot',
			'ROTATOR',
			'step not on pets.',
			'MADAM I\'M ADAM',
			'no lemon, NO Melon'
			'No LeMoN, nomelon',
			'Able was I, ere I saw Elba!',
			'Was it a car or a cat I saw',
			'Eine treue Familie bei Lima feuerte nie',
			'Die Liebe ist Sieger; stets rege ist sie bei Leid',
			'O Genie, der Herr ehre Dein Ego',
			'Elu par cette crapule',
			'Tu l\'as trop ecrase cesar ce port salut.',
			'A l\'autel elle alla, elle le tua la',
			'Caser vite ce palindrome ne mord ni lape cet ivre sac',
			'isälläsi',
			'Ana, kanna kana',
			'Hupaisa asia, Puh',
			'Isorikas sika sökösakissa kirosi',
			'I jogurt ujutru goji?',
			'УЈАК ИМА РАДАР  А МИ КАЈУ',
			'око',
			'12321'
			
        ]
		self.valid_check(valid_items)
		print('OK - test_valid_palindrome')

	def test_invalid_palindrome(self):
		invalid_items = [
			'asd',
			'hello, world'
			'this is not a palindrome',
			'12345',
			'ок0'
			
        ]
		self.invalid_check(invalid_items)
		print('OK - test_invalid_palindrome')

	def test_invalid_case_sensitive_palindrome(self):
		invalid_items = [
			'No LeMoN, nomelon',
			'Was it a car or a cat I saw',
			'isäLläSi',
        ]
		self.invalid_check(invalid_items, { "insensitive": False })
		print('OK - test_invalid_case_sensitive_palindrome')
