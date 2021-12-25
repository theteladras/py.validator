from .is_float import is_float
from .is_int import is_int

def is_number(input: str) -> bool:
    is_input_float = is_float(input) or is_float(input, { "locale": "ar" })
    is_input_int = is_int(input)
    if is_input_float or is_input_int:
        return True
    return False
