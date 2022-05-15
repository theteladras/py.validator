import unittest

from pyvalidator.is_slug import is_slug
from . import print_test_ok


class TestIsSlug(unittest.TestCase):

    def test_valid_slug(self):
        for i in [
            'foo',
            'foo-bar',
            'foo_bar',
            'foo-bar-foo',
            'foo-bar_foo',
            'foo-bar_foo*75-b4r-**_foo',
            'foo-bar_foo*75-b4r-**_foo-&&',
        ]:
            self.assertTrue(is_slug(i))
        print_test_ok()

    def test_invalid_slug(self):
        for i in [
            'not-----------slug',
            '@#_$@',
            '-not-slug',
            'not-slug-',
            '_not-slug',
            'not-slug_',
            'not slug',
        ]:
            self.assertFalse(is_slug(i))
        print_test_ok()
