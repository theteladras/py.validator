from .Classes.String import String


def assert_string(input: str) -> String:
    is_string = type(input).__name__ == 'str' or isinstance(input, str)

    if not is_string:
        invalid_type = type(input).__name__
        raise ValueError(f"Expected a string but received a {invalid_type}")

    return String(input)
