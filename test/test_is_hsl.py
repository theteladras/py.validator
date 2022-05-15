import unittest

from pyvalidator.is_hsl import is_hsl
from . import print_test_ok


class TestIsHsl(unittest.TestCase):

    def test_valid_hsl(self):
        for i in [
            'hsl(360,0000000000100%,000000100%)',
            'hsl(000010, 00000000001%, 00000040%)',
            'HSL(00000,0000000000100%,000000100%)',
            'hsL(0, 0%, 0%)',
            'hSl(  360  , 100%  , 100%   )',
            'Hsl(  00150  , 000099%  , 01%   )',
            'hsl(01080, 03%, 4%)',
            'hsl(-540, 03%, 4%)',
            'hsla(+540, 03%, 4%)',
            'hsla(+540, 03%, 4%, 500)',
            'hsl(+540deg, 03%, 4%, 500)',
            'hsl(+540gRaD, 03%, 4%, 500)',
            'hsl(+540.01e-98rad, 03%, 4%, 500)',
            'hsl(-540.5turn, 03%, 4%, 500)',
            'hsl(+540, 03%, 4%, 500e-01)',
            'hsl(+540, 03%, 4%, 500e+80)',
            'hsl(4.71239rad, 60%, 70%)',
            'hsl(270deg, 60%, 70%)',
            'hsl(200, +.1%, 62%, 1)',
            'hsl(270 60% 70%)',
            'hsl(200, +.1e-9%, 62e10%, 1)',
            'hsl(.75turn, 60%, 70%)',
            'hsl(200grad +.1% 62% / 1)',
            'hsl(270, 60%, 50%, .15)',
            'hsl(270, 60%, 50%, 15%)',
            'hsl(270 60% 50% / .15)',
            'hsl(270 60% 50% / 15%)',
        ]:
            self.assertTrue(is_hsl(i))
        print_test_ok()

    def test_invalid_hsl(self):
        for i in [
            'hsl (360,0000000000100%,000000100%)',
            'hsl(0260, 100 %, 100%)',
            'hsl(0160, 100%, 100%, 100 %)',
            'hsl(-0160, 100%, 100a)',
            'hsl(-0160, 100%, 100)',
            'hsl(-0160 100%, 100%, )',
            'hsl(270 deg, 60%, 70%)',
            'hsl( deg, 60%, 70%)',
            'hsl(, 60%, 70%)',
            'hsl(3000deg, 70%)',
        ]:
            self.assertFalse(is_hsl(i))
        print_test_ok()
