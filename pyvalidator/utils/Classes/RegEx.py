import re
from typing import AnyStr, Literal, Pattern, Union

from .List import List

FlagType = Union[Literal["g"], Literal["i"], Literal["m"], Literal["u"], None]


class RegEx(object):
    pattern = None
    raw_pattern = None

    def __init__(self, pattern: str, flag: FlagType = None) -> None:
        raw_pattern = pattern
        if not pattern:
            raise ValueError("Pattern not provided")
        self.compile_pattern(pattern, flag)

    def compile_pattern(self, pattern: str, flag: FlagType) -> None:
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

    def split(self, input: str) -> List:
        return List(re.split(self.pattern, input))

    @staticmethod
    def sub(pattern: str, replacement: str, input: str) -> str:
        return re.sub(pattern, replacement, input)

    @staticmethod
    def escape(input: str) -> str:
        return re.escape(input)

    def findall(self, target: str) -> Union[List, None]:
        matches = re.findall(self.pattern, target)
        if not len(matches):
            return None
        return re.findall(self.pattern, target)

    @staticmethod
    def compile(pattern) -> Pattern[AnyStr]:
        return re.compile(pattern)

    def search(self, target: str) -> Union[int, None]:
        return re.search(self.pattern, target).start()
