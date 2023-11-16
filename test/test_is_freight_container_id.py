import unittest
from pyvalidator.is_freight_container_id import is_freight_container_id
from . import print_test_ok

class TestIsFreightContainerId(unittest.TestCase):

    def test_valid_ISO6346(self):
        valid_codes = [
            'HLXU2008419',
			'TGHU7599330',
			'ECMU4657496',
			'MEDU6246078',
			'YMLU2809976',
			'MRKU0046221',
			'EMCU3811879',
			'OOLU8643084',
			'HJCU1922713',
			'QJRZ123456',
        ]
        for code in valid_codes:
            self.assertTrue(is_freight_container_id(code))
        print_test_ok()

    def test_invalid_ISO6346(self):
        invalid_codes = [
            'OOLU1922713',
			'HJCU1922413',
			'FCUI985619',
			'ECMJ4657496',
			'TBJA7176445',
			'AFFU5962593',
        ]
        for code in invalid_codes:
            self.assertFalse(is_freight_container_id(code))
        print_test_ok()

if __name__ == '__main__':
    unittest.main()
