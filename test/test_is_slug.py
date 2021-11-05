import unittest
from validator import *

class TestIsSlug(unittest.TestCase):

    def test_valid_slug(self):
        self.assertTrue(is_slug('foo'))
        self.assertTrue(is_slug('foo-bar'))
        self.assertTrue(is_slug('foo_bar'))
        self.assertTrue(is_slug('foo-bar-foo'))
        self.assertTrue(is_slug('foo-bar_foo'))
        self.assertTrue(is_slug('foo-bar_foo*75-b4r-**_foo'))
        self.assertTrue(is_slug('foo-bar_foo*75-b4r-**_foo-&&'))
        print('OK - test_valid_slug')

    def test_invalid_slug(self):
        self.assertFalse(is_slug('not-----------slug'))
        self.assertFalse(is_slug('@#_$@'))
        self.assertFalse(is_slug('-not-slug'))
        self.assertFalse(is_slug('not-slug-'))
        self.assertFalse(is_slug('_not-slug'))
        self.assertFalse(is_slug('not-slug_'))
        self.assertFalse(is_slug('not slug'))
        print('OK - test_invalid_slug')
