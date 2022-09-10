import unittest

from pyvalidator.is_license_plate import is_license_plate
from . import print_test_ok


class TestIsLicensePlate(unittest.TestCase):

    def test_valid_license_plate_pt_PT(self):
        for i in [
            'AA-12-34',
            '12·34·AB',
            '12·AB·34',
            'AB 12 CD',
            'AB12CD',
        ]:
            self.assertTrue(is_license_plate(i, 'pt-PT'))
        print_test_ok()

    def test_invalid_license_plate_pt_PT(self):
        for i in [
            '',
            'notalicenseplate',
            'A1-B2-C3',
            'ABC-1-EF',
        ]:
            self.assertFalse(is_license_plate(i, 'pt-PT'))
        print_test_ok()

    def test_valid_license_plate_de_LI(self):
        for i in [
            'FL 1',
            'FL 99999',
            'FL 1337'
        ]:
            self.assertTrue(is_license_plate(i, 'de-LI'))
        print_test_ok()

    def test_invalid_license_plate_de_LI(self):
        for i in [
            '',
            'FL 999999',
            'AB 12345',
            'FL -1',
        ]:
            self.assertFalse(is_license_plate(i, 'de-LI'))
        print_test_ok()

    def test_valid_license_plate_de_DE(self):
        for i in [
            'M A 1',
            'M A 12',
            'M A 123',
            'M A 1234',
            'M AB 1',
            'M AB 12',
            'M AB 123',
            'M AB 1234',
            'FS A 1',
            'FS A 12',
            'FS A 123',
            'FS A 1234',
            'FS AB 1',
            'FS AB 12',
            'FS AB 123',
            'FS AB 1234',
            'FSAB1234',
            'FS-AB-1234',
            'FS AB 1234 H',
            'FS AB 1234 E',
            'FSAB1234E',
            'FS-AB-1234-E',
            'FS AB-1234-E',
            'FSAB1234 E',
            'FS AB1234E',
            'LRO AB 123',
            'LRO-AB-123-E',
            'LRO-AB-123E',
            'LRO-AB-123 E',
            'LRO-AB-123-H',
            'LRO-AB-123H',
            'LRO-AB-123 H',
        ]:
            self.assertTrue(is_license_plate(i, 'de-DE'))
        print_test_ok()

    def test_invalid_license_plate_de_DE(self):
        for i in [
            'YY AB 123',
            'PAF AB 1234',
            'M ABC 123',
            'M AB 12345',
            'FS AB 1234 A',
            'LRO-AB-1234',
            'HRO ABC 123',
            'HRO ABC 1234',
            'LDK-AB-1234-E',
            'ÖHR FA 123D',
            'MZG-AB-123X',
            'OBG-ABD-123',
            'PAF-AB2-123',
        ]:
            self.assertFalse(is_license_plate(i, 'de-DE'))
        print_test_ok()

    def test_valid_license_plate_fi_FI(self):
        for i in [
            'ABC-123',
            'ABC 123',
            'ABC123',
            'A100',
            'A 100',
            'A-100',
            'C10001',
            'C 10001',
            'C-10001',
            '123-ABC',
            '123 ABC',
            '123ABC',
            '123-A',
            '123 A',
            '123A',
            '199AA',
            '199 AA',
            '199-AA',
        ]:
            self.assertTrue(is_license_plate(i, 'fi-FI'))
        print_test_ok()

    def test_invalid_license_plate_fi_FI(self):
        for i in [
            ' ',
            'A-1',
            'A1A-100',
            '1-A-2',
            'C1234567',
            'A B C 1 2 3',
            'abc-123',
        ]:
            self.assertFalse(is_license_plate(i, 'fi-FI'))
        print_test_ok()

    def test_valid_license_plate_sq_AL(self):
        for i in [
            'AA 000 AA',
            'ZZ 999 ZZ',
        ]:
            self.assertTrue(is_license_plate(i, 'sq-AL'))
        print_test_ok()

    def test_invalid_license_plate_sq_AL(self):
        for i in [
            '',
            'AA 0 A',
            'AAA 00 AAA',
        ]:
            self.assertFalse(is_license_plate(i, 'sq-AL'))
        print_test_ok()

    def test_valid_license_plate_cs_CZ(self):
        for i in [
            'ALA4011',
            '4A23000',
            'DICTAT0R',
            'VETERAN',
            'AZKVIZ8',
            '2A45876',
            'DIC-TAT0R',
        ]:
            self.assertTrue(is_license_plate(i, 'cs-CZ'))
        print_test_ok()

    def test_invalid_license_plate_cs_CZ(self):
        for i in [
            '',
            'invalidlicenseplate',
            'LN5758898',
            'X-|$|-X',
            'AE0F-OP4',
            'GO0MER',
            '2AAAAAAAA',
            'FS AB 1234 E',
            'GB999 9999 00',
        ]:
            self.assertFalse(is_license_plate(i, 'cs-CZ'))
        print_test_ok()

    def test_valid_license_plate_pt_BR(self):
        for i in [
            'ABC1234',
            'ABC 1234',
            'ABC-1234',
            'ABC1D23',
            'ABC1K23',
            'ABC1Z23',
            'ABC 1D23',
            'ABC-1D23',
        ]:
            self.assertTrue(is_license_plate(i, 'pt-BR'))
        print_test_ok()

    def test_invalid_license_plate_pt_BR(self):
        for i in [
            '',
            'AA 0 A',
            'AAA 00 AAA',
            'ABCD123',
            'AB12345',
            'AB123DC',
        ]:
            self.assertFalse(is_license_plate(i, 'pt-BR'))
        print_test_ok()

    def test_valid_license_plate_sr_RS(self):
        for i in [
            'BG 1234 AZ',
            'BG 123 AZ',
            'BG-123-AZ',
            'BG123AZ',
            'VŠ123VŠ',
            'BG 094 ĆM',
            'BG-12456',
            'П555333'
        ]:
            self.assertTrue(is_license_plate(i, 'sr-RS'))
        print_test_ok()

    def test_invalid_license_plate_sr_RS(self):
        for i in [
            '',
            ' ',
            'AAA 00 AAA',
            'AB123DC',
            'AB-123-VŠ',
            'BG-123_AZ',
            'BG_123_AZ',
            'BG-12-AZ',
            'BG-12456-AZ',
            'BG 123 AÜ',
            'BG-124563',
            'П2233'
        ]:
            self.assertFalse(is_license_plate(i, 'sr-RS'))
        print_test_ok()

    def test_valid_license_plate_any(self):
        for i in [
            'ABC1234',
            'ABC 1234',
            'ABC-1234',
            'ABC1D23',
            'ABC1K23',
            'ABC1Z23',
            'ABC 1D23',
            'ABC-1D23',
            'FL 1',
            'FS AB 123',
        ]:
            self.assertTrue(is_license_plate(i))
        print_test_ok()

    def test_invalid_license_plate_any(self):
        for i in [
            '',
            'FL 999999',
            'FS AB 1234 A',
            'notalicenseplate',
        ]:
            self.assertFalse(is_license_plate(i))
        print_test_ok()

    def test_invalid_license_plate_any(self):
        for i in [
            'ABC-1D23',
            'FL 1',
        ]:
            self.assertRaises(Exception, is_license_plate, i, 'asd')
        print_test_ok()
