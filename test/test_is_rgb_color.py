import unittest
from validator import *

class TestIsRgbColor(unittest.TestCase):

    def test_valid_rgb_color(self):
        self.assertTrue(is_rgb_color('rgb(0,0,0)'))
        self.assertTrue(is_rgb_color('rgb(255,255,255)'))
        self.assertTrue(is_rgb_color('rgba(0,0,0,0)'))
        self.assertTrue(is_rgb_color('rgba(255,255,255,1)'))
        self.assertTrue(is_rgb_color('rgba(255,255,255,.1)'))
        self.assertTrue(is_rgb_color('rgba(255,255,255,0.1)'))
        self.assertTrue(is_rgb_color('rgb(5%,5%,5%)'))
        self.assertTrue(is_rgb_color('rgba(5%,5%,5%,.3)'))
        print('OK - test_valid_rgb_color')

    def test_invalid_rgb_color(self):
        self.assertFalse(is_rgb_color('rgb(0,0,0,)'))
        self.assertFalse(is_rgb_color('rgb(0,0,)'))
        self.assertFalse(is_rgb_color('rgb(0,0,256)'))
        self.assertFalse(is_rgb_color('rgb()'))
        self.assertFalse(is_rgb_color('rgba(0,0,0)'))
        self.assertFalse(is_rgb_color('rgba(255,255,255,2)'))
        self.assertFalse(is_rgb_color('rgba(255,255,255,.12)'))
        self.assertFalse(is_rgb_color('rgba(255,255,256,0.1)'))
        self.assertFalse(is_rgb_color('rgb(4,4,5%)'))
        self.assertFalse(is_rgb_color('rgba(5%,5%,5%)'))
        self.assertFalse(is_rgb_color('rgba(3,3,3%,.3)'))
        self.assertFalse(is_rgb_color('rgb(101%,101%,101%)'))
        self.assertFalse(is_rgb_color('rgba(3%,3%,101%,0.3)'))
        print('OK - test_invalid_rgb_color')

    def test_valid_rgb_color_no_percent(self):
        self.assertTrue(is_rgb_color('rgb(1,1,1)', False))
        self.assertTrue(is_rgb_color('rgba(5,5,5,.3)', False))
        print('OK - test_valid_rgb_color_no_percent')

    def test_invalid_rgb_color_no_percent(self):
        self.assertFalse(is_rgb_color('rgb(4,4,5%)', False))
        self.assertFalse(is_rgb_color('rgba(1%,1%,1%)', False))
        print('OK - test_invalid_rgb_color_no_percent')
