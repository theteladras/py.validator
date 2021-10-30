from typing import Union

import re

from .utils.assert_string import assert_string

uuid = {
  "1": re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-1[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}$", re.IGNORECASE),
  "2": re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-2[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}$", re.IGNORECASE),
  "3": re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-3[0-9A-F]{3}-[0-9A-F]{4}-[0-9A-F]{12}$", re.IGNORECASE),
  "4": re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$", re.IGNORECASE),
  "5": re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-5[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$", re.IGNORECASE),
  "all": re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$", re.IGNORECASE),
}

def is_uuid(input: str, version: Union["0", "1", "2", "3", "4", "5", "all", None] = "all") -> bool:
    input = assert_string(input)

    if version not in uuid:
        return False

    pattern = uuid[version]
    return bool(pattern) and bool(pattern.match(input))
