import unittest
from validator import *

class TestIsDataUri(unittest.TestCase):

    def test_valid_data_uri(self):
        self.assertTrue(is_data_uri('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        self.assertTrue(is_data_uri('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAFVBMVEXk5OTn5+ft7e319fX29vb5+fn///++GUmVAAAALUlEQVQIHWNICnYLZnALTgpmMGYIFWYIZTA2ZFAzTTFlSDFVMwVyQhmAwsYMAKDaBy0axX/iAAAAAElFTkSuQmCC'))
        self.assertTrue(is_data_uri('   data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAFVBMVEXk5OTn5+ft7e319fX29vb5+fn///++GUmVAAAALUlEQVQIHWNICnYLZnALTgpmMGYIFWYIZTA2ZFAzTTFlSDFVMwVyQhmAwsYMAKDaBy0axX/iAAAAAElFTkSuQmCC   '))
        self.assertTrue(is_data_uri('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22100%22%20height%3D%22100%22%3E%3Crect%20fill%3D%22%2300B1FF%22%20width%3D%22100%22%20height%3D%22100%22%2F%3E%3C%2Fsvg%3E'))
        self.assertTrue(is_data_uri('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48cmVjdCBmaWxsPSIjMDBCMUZGIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIvPjwvc3ZnPg=='))
        self.assertTrue(is_data_uri(' data:,Hello%2C%20World!'))
        self.assertTrue(is_data_uri(' data:,Hello World!'))
        self.assertTrue(is_data_uri(' data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D'))
        self.assertTrue(is_data_uri(' data:text/html,%3Ch1%3EHello%2C%20World!%3C%2Fh1%3E'))
        self.assertTrue(is_data_uri('data:,A%20brief%20note'))
        self.assertTrue(is_data_uri('data:text/html;charset=US-ASCII,%3Ch1%3EHello!%3C%2Fh1%3E'))
        print('OK - test_valid_data_uri')

    def test_invalid_data_uri(self):
        self.assertFalse(is_data_uri('dataxbase64'))
        self.assertFalse(is_data_uri('data:HelloWorld'))
        self.assertFalse(is_data_uri('data:,A%20brief%20invalid%20[note'))
        self.assertFalse(is_data_uri('file:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D'))
        self.assertFalse(is_data_uri('data:text/html;charset=,%3Ch1%3EHello!%3C%2Fh1%3E'))
        self.assertFalse(is_data_uri('data:text/html;charset,%3Ch1%3EHello!%3C%2Fh1%3E'))
        self.assertFalse(is_data_uri('data:base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        self.assertFalse(is_data_uri(''))
        self.assertFalse(is_data_uri('http://wikipedia.org'))
        self.assertFalse(is_data_uri('base64'))
        self.assertFalse(is_data_uri('iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        print('OK - test_invalid_data_uri')
