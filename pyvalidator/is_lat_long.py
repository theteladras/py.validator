from typing import TypedDict

from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.merge import merge 

lat_pattern = r"^\(?[+-]?(90(\.0+)?|[1-8]?\d(\.\d+)?)$"
long_pattern = r"^\s?[+-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d{1,2}(\.\d+)?)\)?$"

lat_dms_pattern = RegEx(r"^(([1-8]?\d)\D+([1-5]?\d|60)\D+([1-5]?\d|60)(\.\d+)?|90\D+0\D+0)\D+[NSns]?$", "i")
long_dms_pattern = RegEx(r"^\s*([1-7]?\d{1,2}\D+([1-5]?\d|60)\D+([1-5]?\d|60)(\.\d+)?|180\D+0\D+0)\D+[EWew]?$", "i")

class IsLatLongOptions(TypedDict):
    check_dms: bool

__default_options: IsLatLongOptions = {
    "check_dms": False
}

def is_lat_long(input: str, options: IsLatLongOptions = {}) -> bool:
    input = assert_string(input)

    options = merge(options, __default_options)

    if ',' not in input:
        return False
    
    pair = input.split(',')

    if pair.length != 2 or (
        pair[0].startswith('(') and not pair[1].endswith(')') or
        pair[1].endswith(')') and not pair[0].startswith('(')
    ):
        return False

    if options["check_dms"]:
        return pair[0].match(lat_dms_pattern) and pair[1].match(long_dms_pattern)

    return pair[0].match(lat_pattern) and pair[1].match(long_pattern)

