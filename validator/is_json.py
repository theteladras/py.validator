import json
from typing import TypedDict

from .utils.Classes.List import List
from .utils.assert_string import assert_string
from .utils.merge import merge

class IsJsonOptions(TypedDict):
    allow_primitives: str

default_json_options: IsJsonOptions = {
  "allow_primitives": False,
}

def is_json(input: str, options: IsJsonOptions = {}) -> bool:
    input = assert_string(input)
    options = merge(options, default_json_options)
    try:
        parsed = json.loads(input)
        invalid_json_types = List(['int', 'float'])
        if invalid_json_types.includes(type(parsed).__name__):
            return False
        primitives = List(['null', 'false', 'true'])
        if not options["allow_primitives"] and primitives.includes(input):
            return False
        return True
    except:
        return False
