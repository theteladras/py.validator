import inspect


def print_test_ok(extra_string=None):
    print(f"OK - {inspect.stack()[1][3]}{extra_string or ''}")
