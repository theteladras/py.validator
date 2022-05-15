import unittest

from pyvalidator.is_uuid import is_uuid
from . import print_test_ok


class TestIsUuid(unittest.TestCase):

    def test_valid_uuid(self):
        for i in [
            'A987FBC9-4BED-3078-CF07-9141BA07C9F3',
            'A987FBC9-4BED-4078-8F07-9141BA07C9F3',
            'A987FBC9-4BED-5078-AF07-9141BA07C9F3',
        ]:
            self.assertTrue(is_uuid(i))
        print_test_ok()

    def test_invalid_uuid(self):
        for i in [
            '',
            'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3',
            'A987FBC9-4BED-3078-CF07-9141BA07C9F3xxx',
            'A987FBC94BED3078CF079141BA07C9F3',
            '114812',
            ',',
            'foofoo',
            '987FBC9-4BED-3078-CF07A-9141BA07C911',
            'AAAAAAAA-1111-2222-AAAG-111111111111',
        ]:
            self.assertFalse(is_uuid(i))
        print_test_ok()

    def test_valid_uuid_version_1(self):
        for i in [
            ['E034B584-7D89-11E9-9669-1AECF481A97B', "1"],
            ['E034B584-7D89-11E9-9669-1AECF481A97B', 1],
        ]:
            self.assertTrue(is_uuid(*i))
        print_test_ok()

    def test_invalid_uuid_version_1(self):
        for i in [
            ['', "1"],
            ['xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "1"],
            ['AAAAAAAA-1111-2222-AAAG', "1"],
            ['AAAAAAAA-1111-2222-AAAG-111111111111', "1"],
            ['A987FBC9-4BED-4078-8F07-9141BA07C9F3', "1"],
            ['A987FBC9-4BED-5078-AF07-9141BA07C911', "1"],
            ['A987FBC9-4BED-5078-AF07-9141BA07C911', 1],
        ]:
            self.assertFalse(is_uuid(*i))
        print_test_ok()

    def test_valid_uuid_version_2(self):
        for i in [
            ['A117FBC9-4BED-2078-CF07-9141BA07C9F3', "2"],
            ['A117FBC9-4BED-2078-CF07-9141BA07C9F3', 2],
        ]:
            self.assertTrue(is_uuid(*i))
        print_test_ok()

    def test_invalid_uuid_version_2(self):
        for i in [
            ['', "2"],
            ['xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "2"],
            ['AAAAAAAA-1111-1111-AAAG', "2"],
            ['AAAAAAAA-1111-1111-AAAG-111111111112', "2"],
            ['934859', "2"],
            ['A987FBC9-4BED-5078-AF07-9141BA07C911', "2"],
            ['A987FBC9-4BED-5078-AF07-9141BA07C9F2', "2"],
            ['A987FBC9-4BED-5078-AF07-9141BA07C9F2', 2],
        ]:
            self.assertFalse(is_uuid(*i))
        print_test_ok()

    def test_valid_uuid_version_3(self):
        for i in [
            ['1987FBC9-4BED-3078-CF07-9141BA07C9F3', "3"],
            ['1987FBC9-4BED-3078-CF07-9141BA07C9F3', 3],
        ]:
            self.assertTrue(is_uuid(*i))
        print_test_ok()

    def test_invalid_uuid_version_3(self):
        for i in [
            ['', "3"],
            ['xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "3"],
            ['AAAAAAAA-1111-1111-AAAG-111111111112', "3"],
            ['934859', "3"],
            ['A987FBC9-4BED-4078-8F07-9141BA07C9F3', "3"],
            ['A987FBC9-4BED-5078-8F07-9141BA07C9F3', "3"],
        ]:
            self.assertFalse(is_uuid(*i))
        print_test_ok()

    def test_valid_uuid_version_4(self):
        for i in [
            ['713ae7e3-cb32-45f9-adcb-7c4fa86b90c1', "4"],
            ['625e63f3-58f5-40b7-83a1-a72ad31acffb', "4"],
            ['57b73598-8764-4ad0-a76a-679bb6640eb1', "4"],
            ['9c858901-8a57-4791-81fe-4c455b099bc9', "4"],
        ]:
            self.assertTrue(is_uuid(*i))
        print_test_ok()

    def test_invalid_uuid_version_4(self):
        for i in [
            ['', "4"],
            ['xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "4"],
            ['AAAAAAAA-1111-1111-AAAG-111111111112', "4"],
            ['934859', "4"],
            ['A987FBC9-4BED-3078-8F07-9141BA07C9F3', "4"],
            ['A987FBC9-4BED-5078-8F07-9141BA07C9F3', "4"],
        ]:
            self.assertFalse(is_uuid(*i))
        print_test_ok()

    def test_valid_uuid_version_5(self):
        for i in [
            ['987FBC97-4BED-5078-AF07-9141BA07C9F3', "5"],
            ['987FBC97-4BED-5078-BF07-9141BA07C9F3', "5"],
            ['987FBC97-4BED-5078-8F07-9141BA07C9F3', "5"],
            ['987FBC97-4BED-5078-9F07-9141BA07C9F3', "5"],
            ['987FBC97-4BED-5078-9F07-9141BA07C9F3', 5],
        ]:
            self.assertTrue(is_uuid(*i))
        print_test_ok()

    def test_invalid_uuid_version_5(self):
        for i in [
            ['', "5"],
            ['xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3', "5"],
            ['934859', "5"],
            ['AAAAAAAA-1111-1111-AAAG-111111111111', "5"],
            ['9c858901-8a57-4791-81fe-4c455b099bc9', "5"],
            ['A987FBC9-4BED-3078-CF07-9141BA07C9F3', "5"],
        ]:
            self.assertFalse(is_uuid(*i))
        print_test_ok()

    def test_invalid_uuid_version_6(self):
        for i in [
            ['987FBC97-4BED-1078-AF07-9141BA07C9F3', "6"],
            ['987FBC97-4BED-2078-AF07-9141BA07C9F3', "6"],
            ['987FBC97-4BED-3078-AF07-9141BA07C9F3', "6"],
            ['987FBC97-4BED-4078-AF07-9141BA07C9F3', "6"],
            ['987FBC97-4BED-5078-AF07-9141BA07C9F3', "6"],
        ]:
            self.assertFalse(is_uuid(*i))
        print_test_ok()
