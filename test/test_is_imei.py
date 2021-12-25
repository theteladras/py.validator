import unittest
from pyvalidator import *

class TestIsImei(unittest.TestCase):

    def test_valid_imei(self):
        self.assertTrue(is_imei('352099001761481'))
        self.assertTrue(is_imei('868932036356090'))
        self.assertTrue(is_imei('490154203237518'))
        self.assertTrue(is_imei('546918475942169'))
        self.assertTrue(is_imei('998227667144730'))
        self.assertTrue(is_imei('532729766805999'))
        print('OK - test_valid_imei')

    def test_invalid_imei(self):
        self.assertFalse(is_imei('490154203237517'))
        self.assertFalse(is_imei('3568680000414120'))
        self.assertFalse(is_imei('3520990017614823'))
        print('OK - test_invalid_imei')

    def test_valid_imei_with_hyphens(self):
        self.assertTrue(is_imei('35-209900-176148-1', { "allow_hyphens": True }))
        self.assertTrue(is_imei('86-893203-635609-0', { "allow_hyphens": True }))
        self.assertTrue(is_imei('49-015420-323751-8', { "allow_hyphens": True }))
        self.assertTrue(is_imei('54-691847-594216-9', { "allow_hyphens": True }))
        self.assertTrue(is_imei('99-822766-714473-0', { "allow_hyphens": True }))
        self.assertTrue(is_imei('53-272976-680599-9', { "allow_hyphens": True }))
        print('OK - test_valid_imei_with_hyphens')

    def test_invalid_imei_with_hyphens(self):
        self.assertFalse(is_imei('49-015420-323751-7', { "allow_hyphens": True }))
        self.assertFalse(is_imei('35-686800-0041412-0', { "allow_hyphens": True }))
        self.assertFalse(is_imei('35-209900-1761482-3', { "allow_hyphens": True }))
        self.assertFalse(is_imei('3520990017614823', { "allow_hyphens": True }))
        print('OK - test_invalid_imei_with_hyphens')
