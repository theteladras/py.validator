import unittest

from pyvalidator.is_mime_type import is_mime_type
from . import print_test_ok


class TestIsMimeType(unittest.TestCase):

    def test_valid_mime_type(self):
        for i in [
            'application/json',
            'application/xhtml+xml',
            'audio/mp4',
            'image/bmp',
            'font/woff2',
            'message/http',
            'model/vnd.gtw',
            'application/media_control+xml',
            'multipart/form-data',
            'multipart/form-data; boundary=something',
            'multipart/form-data; charset=utf-8; boundary=something',
            'multipart/form-data; boundary=something; charset=utf-8',
            'multipart/form-data; boundary=something; charset="utf-8"',
            'multipart/form-data; boundary="something"; charset=utf-8',
            'multipart/form-data; boundary="something"; charset="utf-8"',
            'text/css',
            'text/plain; charset=utf8',
            'Text/HTML;Charset="utf-8"',
            'text/html;charset=UTF-8',
            'Text/html;charset=UTF-8',
            'text/html; charset=us-ascii',
            'text/html; charset=us-ascii (Plain text)',
            'text/html; charset="us-ascii"',
            'video/mp4',
        ]:
            self.assertTrue(is_mime_type(i), i)
        print_test_ok()

    def test_invalid_mime_type(self):
        for i in [
            '',
            ' ',
            '/',
            'f/b',
            'application',
            'application\\json',
            'application/json/text',
            'application/json; charset=utf-8',
            'audio/mp4; charset=utf-8',
            'image/bmp; charset=utf-8',
            'font/woff2; charset=utf-8',
            'message/http; charset=utf-8',
            'model/vnd.gtw; charset=utf-8',
            'video/mp4; charset=utf-8',
        ]:
            self.assertFalse(is_mime_type(i), i)
        print_test_ok()
