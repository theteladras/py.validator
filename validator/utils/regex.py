import re

class RegEx(object):
    pattern = None

    def __init__(self, pattern: str) -> None:
        if not pattern:
            raise Exception("Pattern not provided")
        self.pattern = re.compile(pattern)

    def match(self, input: str) -> bool:
        if not self.pattern:
            return False
        return bool(self.pattern.match(input))
