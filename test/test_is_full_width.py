import unittest

from pyvalidator.is_full_width import is_full_width
from . import print_test_ok


class TestIsFullWidth(unittest.TestCase):

    def test_valid_full_width(self):
        for i in [
            'ひらがな・カタカナ、．漢字',
            '３ー０　ａ＠ｃｏｍ',
            'Ｆｶﾀｶﾅﾞﾬ',
            'Ğood＝Parts',
        ]:
            self.assertTrue(is_full_width(i))
        print_test_ok()

    def test_invalid_full_width(self):
        for i in [
            'abc',
            'abc123',
            '!"#$%&()<>/+=-_? ~^|.,@`{}[]',
        ]:
            self.assertFalse(is_full_width(i))
        print_test_ok()
