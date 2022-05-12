import inspect


def print_test_ok(extra_string=None):
    msg = f"OK - {inspect.stack()[1][3]}"
    if extra_string:
        msg += f" {extra_string}"
    print(msg)
