import unittest
import validator

class TestIsMongoId(unittest.TestCase):

    def test_valid_mongo_id(self):
        self.assertTrue(validator.is_mongo_id('507f1f77bcf86cd799439011'))
        self.assertTrue(validator.is_mongo_id('5349b4ddd2781d08c09890f3'))
        self.assertTrue(validator.is_mongo_id('5349b4ddd2781d08c09890f4'))
        print('OK - test_valid_mongo_id')

    def test_invalid_mongo_id(self):
        self.assertFalse(validator.is_mongo_id(''))
        self.assertFalse(validator.is_mongo_id('.'))
        self.assertFalse(validator.is_mongo_id('                        '))
        self.assertFalse(validator.is_mongo_id('507f1f77bcf86cd7994390'))
        self.assertFalse(validator.is_mongo_id('507f1f77bcf86cd79943901z'))
        self.assertFalse(validator.is_mongo_id(' 507f1f77bcf86cd799439011'))
        self.assertFalse(validator.is_mongo_id('507f1f77bcf86cd799439011 '))
        print('OK - test_invalid_mongo_id')