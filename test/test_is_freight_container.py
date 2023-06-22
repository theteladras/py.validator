import unittest
from unittest import result

from pyvalidator.is_freight_container import is_valid_container_number
from . import print_test_ok

class ContainerNumberValidationTest(unittest.TestCase):
    def test_valid_container_number(self):
        container_number = "ASDD123456"
        result = is_valid_container_number(container_number)
        self.assertTrue(result)
        print_test_ok

    def test_invalid_container_number(self):
        container_number = "DA123456"
        result = is_valid_container_number(container_number)
        self.assertFalse(result)
        print_test_ok
