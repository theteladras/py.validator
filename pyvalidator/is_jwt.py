from .utils.assert_string import assert_string
from .is_base64 import is_base64

def is_jwt(input: str) -> bool:
    input = assert_string(input)

    dot_split = input.split('.')
    length = dot_split.length

    if length < 2 or length > 3:
        return False

    def reducer(acc: bool, curr: bool) -> bool:
        return acc and is_base64(curr, { "url_safe": True })

    return dot_split.reduce(reducer, True)
