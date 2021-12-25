from typing import Literal

from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.slice import slice
from .utils.Classes.String import String
from .is_number import is_number

LENGTH_EAN_8 = 8
LENGTH_EAN_14 = 14
valid_ean_regex = RegEx("^(\d{8}|\d{13}|\d{14})$")

def get_position_weight_through_length_and_index(length: int, index: int) -> Literal[1, 3]:
    if length == LENGTH_EAN_8 or length == LENGTH_EAN_14:
        return 3 if (index % 2 == 0) else 1
    return 1 if (index % 2 == 0) else 3

def calculate_check_digit(ean: String) -> int:
    def iterator(char, index):
        return int(char) * get_position_weight_through_length_and_index(ean.length, index)

    def reducer(acc, partial_sum):
        return acc + partial_sum
    
    check_sum = ean.slice(0, -1).split().map(iterator).reduce(reducer, 0)

    remainder = 10 - (check_sum % 10)

    return remainder if remainder < 10 else 0

def is_ean(input: str) -> bool:
    input = assert_string(input)

    actual_check_digit = input.slice(-1)
    if not is_number(actual_check_digit):
        return False
    actual_check_digit = int(actual_check_digit)

    input_valid = bool(valid_ean_regex.match(input))

    digits_match = actual_check_digit == calculate_check_digit(input)
    
    return input_valid and digits_match

