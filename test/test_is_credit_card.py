import unittest
from pyvalidator import *

class TestIsCreditCard(unittest.TestCase):

    def test_valid_credit_cards(self):
        self.assertTrue(is_credit_card('375556917985515'))
        self.assertTrue(is_credit_card('36050234196908'))
        self.assertTrue(is_credit_card('4716461583322103'))
        self.assertTrue(is_credit_card('4716-2210-5188-5662'))
        self.assertTrue(is_credit_card('4929 7226 5379 7141'))
        self.assertTrue(is_credit_card('5398228707871527'))
        self.assertTrue(is_credit_card('6283875070985593'))
        self.assertTrue(is_credit_card('6263892624162870'))
        self.assertTrue(is_credit_card('6234917882863855'))
        self.assertTrue(is_credit_card('6234698580215388'))
        self.assertTrue(is_credit_card('6226050967750613'))
        self.assertTrue(is_credit_card('6246281879460688'))
        self.assertTrue(is_credit_card('2222155765072228'))
        self.assertTrue(is_credit_card('2225855203075256'))
        self.assertTrue(is_credit_card('2720428011723762'))
        self.assertTrue(is_credit_card('2718760626256570'))
        self.assertTrue(is_credit_card('6765780016990268'))
        self.assertTrue(is_credit_card('4716989580001715211'))
        self.assertTrue(is_credit_card('8171999927660000'))
        self.assertTrue(is_credit_card('8171999900000000021'))
        print('OK - test_valid_credit_cards')

    def test_invalid_credit_cards(self):
        self.assertFalse(is_credit_card('foo'))
        self.assertFalse(is_credit_card('5398228707871528'))
        self.assertFalse(is_credit_card('2718760626256571'))
        self.assertFalse(is_credit_card('2721465526338453'))
        self.assertFalse(is_credit_card('2220175103860763'))
        self.assertFalse(is_credit_card('375556917985515999999993'))
        self.assertFalse(is_credit_card('899999996234917882863855'))
        self.assertFalse(is_credit_card('prefix6234917882863855'))
        self.assertFalse(is_credit_card('6234917882863855suffix'))
        self.assertFalse(is_credit_card('4716989580001715213'))
        print('OK - test_invalid_credit_cards')
