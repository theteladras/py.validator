import re
from typing import Literal

class RegEx(object):
    pattern = None

    def __init__(self, pattern: str, flag: Literal["i"] = None) -> None:
        if not pattern:
            raise Exception("Pattern not provided")
        if flag == 'i':
            self.pattern = re.compile(pattern, re.IGNORECASE)
        elif flag == 'g':
            self.pattern = re.compile(pattern, re.DOTALL)
        elif flag == 'm':
            self.pattern = re.compile(pattern, re.MULTILINE)
        elif flag == 'u':
            self.pattern = re.compile(pattern, re.UNICODE)
        else:
            self.pattern = re.compile(pattern)

    def match(self, input: str) -> bool:
        if not self.pattern:
            return False
        return bool(self.pattern.match(input))

    def split(self, input: str) -> list:
        return re.split(self.pattern, input)

    @staticmethod
    def sub(pattern: str, replacement: str, input: str) -> str:
        return re.sub(pattern, replacement, input)

    @staticmethod
    def escape(input: str) -> str:
        return re.escape(input)
