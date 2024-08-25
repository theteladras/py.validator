import unittest
from pyvalidator.is_half_width import is_half_width
from . import print_test_ok

class TestIsHalfWidth(unittest.TestCase):

    def test_valid_half_width(self):
        for i in [
            '!"#$%&()<>/+=-_? ~^|.,@`{}[]',
            'l-btn_02--active',
            'abc123い',
            'ｶﾀｶﾅﾞﾬ￩',
            '!"#$%&()<>/+=-_? ~^|.,@`{}[]'
        ]:
            self.assertTrue(is_half_width(i))
        print_test_ok()

    def test_invalid_half_width(self):
        for i in [
            '３ー０　ａ＠ｃｏｍ'
            'あいうえお',
            '００１１',
            'Ğood＝Parts'
        ]:
            self.assertFalse(is_half_width(i))
        print_test_ok()

if __name__ == '__main__':
    unittest.main()
