import unittest
import inspect

from pyvalidator.utils.to_string import to_string, obj_str
from . import print_test_ok


class TestIsUuid(unittest.TestCase):

    def test_input_str(self):
        self.assertEqual(to_string("x"), "x")
        print_test_ok()

    def test_input_int(self):
        self.assertEqual(to_string(1), "1")
        print_test_ok()

    def test_input_float(self):
        self.assertEqual(to_string(float(1.1)), "1.1")
        print_test_ok()

    def test_input_dict(self):
        self.assertEqual(to_string({"test": 1}), obj_str)
        print_test_ok()

    def test_input_list(self):
        self.assertEqual(to_string([1]), obj_str)
        print_test_ok()

    def test_input_module(self):
        self.assertEqual(to_string(inspect), obj_str)
        print_test_ok()

    def test_input_undefined(self):
        self.assertEqual(to_string(type), '')
        print_test_ok()
