import unittest

from pyvalidator import *


class TestIsUrl(unittest.TestCase):
	def valid_check(self, items, options = {}):
		for item in items:
			try:
				self.assertTrue(is_url(item, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def invalid_check(self, items, options = {}):
		for item in items:
			try:
				self.assertFalse(is_url(item, options))
			except Exception as e:
				print(f'failed for input: {item}')
				raise e

	def test_valid_url(self):
		valid_items = [
            'https://stackoverflow.com/',
			'www.google.com',
            'HTTPS://stackoverflow.com/',
			'www.GOOGLE.com',
			'facebook.com',
			'facebook.COM',
			'http://rs.linkedin.com',
			'test.net',
			'unknowns.cc/yes/please',
			'worldofwarcraft.com/en-gb/game?races=blood-elf',
			'https://seeklogo.com/images/P/pearl-jam-alive-logo-8FA34991E4-seeklogo.com.png',
			'http://api.google.com/q?exp=a%7Cb',
			'https://companydomain.bamboohr.com/authorize.php?request=authorize&state=state&response_type=code&scope=openid&client_id=client_id&redirect_uri=redirecturl',
			'https://id.b2b.yahooinc.com/identity/oauth2/access_token?realm=true_story',
			'https://api.twitter.com/1.1/search/tweets.json',
			'https://api.twitter.com/1.1/search/%20/tweets.json',
			'http://foo.com/blahblah_(wikipedia)',
			'https://test-domain.com/',
			'ha.com',
			'www.go.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzaaaaaaaaaaa'
        ]
		self.valid_check(valid_items)
		print('OK - test_valid_url')

	def test_invalid_url(self):
		invalid_items = [
            '',
            '.',
            'helloworld',
			'127.0.0.1',
			'ffs://silvermoon.com',
			'ffs:/silvermoon.com',
			'/some/random/path',
			'C:\\Documents',
			's.s',
			'http://mw1.google.com/mw-earth-vectordb/kml-samples/gp/seattle/gigapxl/$[level]/r$[y]_c$[x].jpg',
			'http://api.google.com/q?exp=a|b',
			'https://id.b2b.yahooinc.com/identity/oauth2/access_token?realm=true story',
			'https://api.twitter.com/1.1/search/ /tweets.json',
			'http://-test-domain.com',
			'http://test-domain-.com',
			'http://test_domain.com',
			'http://test-domain_.com',
			'http://_test-domain.com',
			'http://test*domain.com',
			'http://test!domain.com',
			'http://test-domain!.com',
			'http://test-domain*.com',
			'hello+world.io',
			'hello=world.io',
			'hello@world.io',
			'hello%world.io',
			'hello:world.io',
			'hello~world.io',
			'h.com',
			'www.go.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzaaaaaaaaaaaa'
        ]
		self.invalid_check(invalid_items)
		print('OK - test_invalid_url')

	def test_valid_url_with_target_domains(self):
		valid_items = [
            'https://stackoverflow.com/',
			'www.google.com',
			'http://api.google.com/q?exp=a%7Cb',
        ]
		self.valid_check(valid_items, { "domains": [ "stackoverflow", "google" ] })
		print('OK - test_valid_url_with_target_domains')

	def test_valid_url_with_target_domain(self):
		valid_items = [
            'https://stackoverflow.com/'
        ]
		self.valid_check(valid_items, { "domains": [ "stackoverflow" ] })
		print('OK - test_valid_url_with_target_domain')

	def test_invalid_url_with_target_domains(self):
		invalid_items = [
            'https://stackoverflow.com/',
			'www.google.com',
			'http://api.google.com/q?exp=a%7Cb',
        ]
		self.invalid_check(invalid_items, { "domains": [ "facebook", "instagram" ] })
		print('OK - test_invalid_url_with_target_domains')

	def test_invalid_url_with_target_domain(self):
		invalid_items = [
            'https://stackoverflow.com/',
			'www.google.com',
			'http://api.google.com/q?exp=a%7Cb'
        ]
		self.invalid_check(invalid_items, { "domains": [ "twitter" ] })
		print('OK - test_invalid_url_with_target_domain')

	def test_valid_url_with_top_level_domains(self):
		items = [
            'https://stackoverflow.com/',
			'www.google.com',
			'en.wikipedia.org'
        ]
		self.valid_check(items, { "top_level_domains": [ "com", "org" ] })
		print('OK - test_valid_url_with_top_level_domains')

	def test_invalid_url_with_top_level_domains(self):
		items = [
            'https://stackoverflow.com/',
			'www.google.com'
        ]
		self.invalid_check(items, { "top_level_domains": [ "net" ] })
		print('OK - test_invalid_url_with_top_level_domains')

	def test_invalid_case_sensitive_url(self):
		items = [
            'HTTPS://stackoverflow.com/',
			'www.google.COM',
			'tWITTer.com'
        ]
		self.invalid_check(items, { "insensitive": False })
		print('OK - test_invalid_case_sensitive_url')

	def test_valid_url_with_no_scheme(self):
		items = [
            'en.wikipedia.org/',
			'www.youtube.com'
        ]
		self.valid_check(items, { "no_scheme": True })
		print('OK - test_valid_url_with_no_scheme')

	def test_invalid_url_with_no_scheme(self):
		items = [
            'https://en.wikipedia.org/',
			'http://www.youtube.com'
        ]
		self.invalid_check(items, { "no_scheme": True })
		print('OK - test_invalid_url_with_no_scheme')

	def test_valid_url_with_no_path(self):
		items = [
            'https://en.wikipedia.org/',
			'https://www.youtube.com'
        ]
		self.valid_check(items, { "with_no_path": True })
		print('OK - test_valid_url_with_no_path')

	def test_invalid_url_for_including_a_path(self):
		items = [
            'https://en.wikipedia.org/wiki/Grunge',
			'https://www.youtube.com/watch?v=iXjMbdHa-IU'
        ]
		self.invalid_check(items, { "with_no_path": True })
		print('OK - test_invalid_case_sensitive_url')
