import unittest

from pyvalidator.is_magnet_uri import is_magnet_uri
from . import print_test_ok


class TestIsMagnetURI(unittest.TestCase):

    def test_valid_magnet_uri(self):
        for i in [
            'magnet:?xt.1=urn:sha1:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456&xt.2=urn:sha1:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456',
            'magnet:?xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234&dn=helloword2000&tr=udp://helloworld:1337/announce',
            'magnet:?xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234&dn=foo',
            'magnet:?xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234&dn=&tr=&nonexisting=hello world',
            'magnet:?xt=urn:md5:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456',
            'magnet:?xt=urn:tree:tiger:ABCDEFGHIJKLMNOPQRSTUVWXYZ123456',
            'magnet:?xt=urn:ed2k:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magnet:?tr=udp://helloworld:1337/announce&xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magnet:?xt=urn:btmh:1220caf1e1c30e81cb361b9ee167c4aa64228a7fa4fa9f6105232b28ad099f3a302e',
        ]:
            self.assertTrue(is_magnet_uri(i))
        print_test_ok()

    def test_invalid_magnet_uri(self):
        for i in [
            ':?xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magneta:?xt=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magnet:?xt=uarn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magnet:?xt=urn:btihz',
            'magnet::?xt=urn:btih:UHWY2892JNEJ2GTEYOMDNU67E8ICGICYE92JDUGH',
            'magnet:?xt:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'magnet:?xt:urn:nonexisting:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magnet:?xt.2=urn:btih:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234',
            'magnet:?xt=urn:ed2k:ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890123456789ABCD',
            'magnet:?xt=urn:btmh:1120caf1e1c30e81cb361b9ee167c4aa64228a7fa4fa9f6105232b28ad099f3a302e',
            'magnet:?ttxt=urn:btmh:1220caf1e1c30e81cb361b9ee167c4aa64228a7fa4fa9f6105232b28ad099f3a302e',
        ]:
            self.assertFalse(is_magnet_uri(i))
        print_test_ok()
