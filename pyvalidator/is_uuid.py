from typing import Union

from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

uuid = {
  "1": RegEx("^[0-9A-F]{8}-[0-9A-F]{4}-1[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}$", "i"),
  "2": RegEx("^[0-9A-F]{8}-[0-9A-F]{4}-2[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}$", "i"),
  "3": RegEx("^[0-9A-F]{8}-[0-9A-F]{4}-3[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}$", "i"),
  "4": RegEx("^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$", "i"),
  "5": RegEx("^[0-9A-F]{8}-[0-9A-F]{4}-5[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$", "i"),
  "all": RegEx("^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$", "i"),
}

def is_uuid(input: str, version: Union["0", "1", "2", "3", "4", "5", "all", None] = "all") -> bool:
    input = assert_string(input)

    version = str(version)

    if version not in uuid:
        return False

    pattern = uuid[version]
    return bool(pattern) and pattern.match(input)
