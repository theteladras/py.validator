import unittest

from pyvalidator.is_mongo_id import is_mongo_id
from . import print_test_ok


class TestIsMongoId(unittest.TestCase):

    def test_valid_mongo_id(self):
        for i in [
            '507f1f77bcf86cd799439011',
            '5349b4ddd2781d08c09890f3',
            '5349b4ddd2781d08c09890f4',
        ]:
            self.assertTrue(is_mongo_id(i))
        print_test_ok()

    def test_invalid_mongo_id(self):
        for i in [
            '',
            '.',
            '                        ',
            '507f1f77bcf86cd7994390',
            '507f1f77bcf86cd79943901z',
            ' 507f1f77bcf86cd799439011',
            '507f1f77bcf86cd799439011 ',
        ]:
            self.assertFalse(is_mongo_id(i))
        print_test_ok()
