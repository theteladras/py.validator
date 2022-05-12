import unittest

from pyvalidator.is_rgb_color import is_rgb_color
from . import print_test_ok


class TestIsRgbColor(unittest.TestCase):

    def test_valid_rgb_color(self):
        for i in [
            'rgb(0,0,0)',
            'rgb(255,255,255)',
            'rgba(0,0,0,0)',
            'rgba(255,255,255,1)',
            'rgba(255,255,255,.1)',
            'rgba(255,255,255,0.1)',
            'rgb(5%,5%,5%)',
            'rgba(5%,5%,5%,.3)',
        ]:
            self.assertTrue(is_rgb_color(i))
        print_test_ok()

    def test_invalid_rgb_color(self):
        for i in [
            'rgb(0,0,0,)',
            'rgb(0,0,)',
            'rgb(0,0,256)',
            'rgb()',
            'rgba(0,0,0)',
            'rgba(255,255,255,2)',
            'rgba(255,255,255,.12)',
            'rgba(255,255,256,0.1)',
            'rgb(4,4,5%)',
            'rgba(5%,5%,5%)',
            'rgba(3,3,3%,.3)',
            'rgb(101%,101%,101%)',
            'rgba(3%,3%,101%,0.3)',
        ]:
            self.assertFalse(is_rgb_color(i))
        print_test_ok()

    def test_valid_rgb_color_no_percent(self):
        for i in [
            'rgb(1,1,1)',
            'rgba(5,5,5,.3)',
        ]:
            self.assertTrue(is_rgb_color(i, False))
        print_test_ok()

    def test_invalid_rgb_color_no_percent(self):
        for i in [
            'rgb(4,4,5%)',
            'rgba(1%,1%,1%)',
        ]:
            self.assertFalse(is_rgb_color(i, False))
        print_test_ok()
