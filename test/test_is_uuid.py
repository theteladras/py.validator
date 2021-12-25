import unittest
from pyvalidator import *

class TestIsUuid(unittest.TestCase):

    def test_valid_uuid(self):
        self.assertTrue(is_uuid('A987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertTrue(is_uuid('A987FBC9-4BED-4078-8F07-9141BA07C9F3'))
        self.assertTrue(is_uuid('A987FBC9-4BED-5078-AF07-9141BA07C9F3'))
        print('OK - test_valid_uuid')

    def test_invalid_uuid(self):
        self.assertFalse(is_uuid(''))
        self.assertFalse(is_uuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertFalse(is_uuid('A987FBC9-4BED-3078-CF07-9141BA07C9F3xxx'))
        self.assertFalse(is_uuid('A987FBC94BED3078CF079141BA07C9F3'))
        self.assertFalse(is_uuid('114812'))
        self.assertFalse(is_uuid(','))
        self.assertFalse(is_uuid('foofoo'))
        self.assertFalse(is_uuid('987FBC9-4BED-3078-CF07A-9141BA07C911'))
        self.assertFalse(is_uuid('AAAAAAAA-1111-2222-AAAG-111111111111'))
        print('OK - test_invalid_uuid')

    def test_valid_uuid_version_1(self):
        self.assertTrue(is_uuid('E034B584-7D89-11E9-9669-1AECF481A97B', "1"))
        self.assertTrue(is_uuid('E034B584-7D89-11E9-9669-1AECF481A97B', 1))
        print('OK - test_valid_uuid_version_1')

    def test_invalid_uuid_version_1(self):
        self.assertFalse(is_uuid('', "1"))
        self.assertFalse(is_uuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "1"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-2222-AAAG', "1"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-2222-AAAG-111111111111', "1"))
        self.assertFalse(is_uuid('A987FBC9-4BED-4078-8F07-9141BA07C9F3', "1"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-AF07-9141BA07C911', "1"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-AF07-9141BA07C911', 1))
        print('OK - test_invalid_uuid_version_1')

    def test_valid_uuid_version_2(self):
        self.assertTrue(is_uuid('A117FBC9-4BED-2078-CF07-9141BA07C9F3', "2"))
        self.assertTrue(is_uuid('A117FBC9-4BED-2078-CF07-9141BA07C9F3', 2))
        print('OK - test_valid_uuid_version_2')

    def test_invalid_uuid_version_2(self):
        self.assertFalse(is_uuid('', "2"))
        self.assertFalse(is_uuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "2"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-1111-AAAG', "2"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-1111-AAAG-111111111112', "2"))
        self.assertFalse(is_uuid('934859', "2"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-AF07-9141BA07C911', "2"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-AF07-9141BA07C9F2', "2"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-AF07-9141BA07C9F2', 2))
        print('OK - test_invalid_uuid_version_2')

    def test_valid_uuid_version_3(self):
        self.assertTrue(is_uuid('1987FBC9-4BED-3078-CF07-9141BA07C9F3', "3"))
        self.assertTrue(is_uuid('1987FBC9-4BED-3078-CF07-9141BA07C9F3', 3))
        print('OK - test_valid_uuid_version_3')

    def test_invalid_uuid_version_3(self):
        self.assertFalse(is_uuid('', "3"))
        self.assertFalse(is_uuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "3"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-1111-AAAG-111111111112', "3"))
        self.assertFalse(is_uuid('934859', "3"))
        self.assertFalse(is_uuid('A987FBC9-4BED-4078-8F07-9141BA07C9F3', "3"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-8F07-9141BA07C9F3', "3"))
        print('OK - test_invalid_uuid_version_3')

    def test_valid_uuid_version_4(self):
        self.assertTrue(is_uuid('713ae7e3-cb32-45f9-adcb-7c4fa86b90c1', "4"))
        self.assertTrue(is_uuid('625e63f3-58f5-40b7-83a1-a72ad31acffb', "4"))
        self.assertTrue(is_uuid('57b73598-8764-4ad0-a76a-679bb6640eb1', "4"))
        self.assertTrue(is_uuid('9c858901-8a57-4791-81fe-4c455b099bc9', "4"))
        print('OK - test_valid_uuid_version_4')

    def test_invalid_uuid_version_4(self):
        self.assertFalse(is_uuid('', "4"))
        self.assertFalse(is_uuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "4"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-1111-AAAG-111111111112', "4"))
        self.assertFalse(is_uuid('934859', "4"))
        self.assertFalse(is_uuid('A987FBC9-4BED-3078-8F07-9141BA07C9F3', "4"))
        self.assertFalse(is_uuid('A987FBC9-4BED-5078-8F07-9141BA07C9F3', "4"))
        print('OK - test_invalid_uuid_version_4')

    def test_valid_uuid_version_5(self):
        self.assertTrue(is_uuid('987FBC97-4BED-5078-AF07-9141BA07C9F3', "5"))
        self.assertTrue(is_uuid('987FBC97-4BED-5078-BF07-9141BA07C9F3', "5"))
        self.assertTrue(is_uuid('987FBC97-4BED-5078-8F07-9141BA07C9F3', "5"))
        self.assertTrue(is_uuid('987FBC97-4BED-5078-9F07-9141BA07C9F3', "5"))
        self.assertTrue(is_uuid('987FBC97-4BED-5078-9F07-9141BA07C9F3', 5))
        print('OK - test_valid_uuid_version_5')

    def test_invalid_uuid_version_5(self):
        self.assertFalse(is_uuid('', "5"))
        self.assertFalse(is_uuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "5"))
        self.assertFalse(is_uuid('934859', "5"))
        self.assertFalse(is_uuid('AAAAAAAA-1111-1111-AAAG-111111111111', "5"))
        self.assertFalse(is_uuid('9c858901-8a57-4791-81fe-4c455b099bc9', "5"))
        self.assertFalse(is_uuid('A987FBC9-4BED-3078-CF07-9141BA07C9F3', "5"))
        print('OK - test_invalid_uuid_version_5')

    def test_invalid_uuid_version_6(self):
        self.assertFalse(is_uuid('987FBC97-4BED-1078-AF07-9141BA07C9F3', "6"))
        self.assertFalse(is_uuid('987FBC97-4BED-2078-AF07-9141BA07C9F3', "6"))
        self.assertFalse(is_uuid('987FBC97-4BED-3078-AF07-9141BA07C9F3', "6"))
        self.assertFalse(is_uuid('987FBC97-4BED-4078-AF07-9141BA07C9F3', "6"))
        self.assertFalse(is_uuid('987FBC97-4BED-5078-AF07-9141BA07C9F3', "6"))
        print('OK - test_invalid_uuid_version_6')
