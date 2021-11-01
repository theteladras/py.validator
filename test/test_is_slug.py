import unittest
import validator

class TestIsSlug(unittest.TestCase):

    def test_valid_slug(self):
        self.assertTrue(validator.is_slug('foo'))
        self.assertTrue(validator.is_slug('foo-bar'))
        self.assertTrue(validator.is_slug('foo_bar'))
        self.assertTrue(validator.is_slug('foo-bar-foo'))
        self.assertTrue(validator.is_slug('foo-bar_foo'))
        self.assertTrue(validator.is_slug('foo-bar_foo*75-b4r-**_foo'))
        self.assertTrue(validator.is_slug('foo-bar_foo*75-b4r-**_foo-&&'))
        print('OK - test_valid_slug')

    def test_invalid_slug(self):
        self.assertFalse(validator.is_slug('not-----------slug'))
        self.assertFalse(validator.is_slug('@#_$@'))
        self.assertFalse(validator.is_slug('-not-slug'))
        self.assertFalse(validator.is_slug('not-slug-'))
        self.assertFalse(validator.is_slug('_not-slug'))
        self.assertFalse(validator.is_slug('not-slug_'))
        self.assertFalse(validator.is_slug('not slug'))
        print('OK - test_invalid_slug')
