import unittest
from validator import *

class TestIsFullWidth(unittest.TestCase):

    def test_valid_full_width(self):
        self.assertTrue(is_full_width('ひらがな・カタカナ、．漢字'))
        self.assertTrue(is_full_width('３ー０　ａ＠ｃｏｍ'))
        self.assertTrue(is_full_width('Ｆｶﾀｶﾅﾞﾬ'))
        self.assertTrue(is_full_width('Ğood＝Parts'))
        print('OK - test_valid_full_width')

    def test_invalid_full_width(self):
        self.assertFalse(is_full_width('abc'))
        self.assertFalse(is_full_width('abc123'))
        self.assertFalse(is_full_width('!"#$%&()<>/+=-_? ~^|.,@`{}[]'))
        print('OK - test_invalid_full_width')
