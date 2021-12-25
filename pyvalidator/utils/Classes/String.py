from typing import TypeVar, Union

from ..slice import slice
from .List import List
from .RegEx import RegEx, FlagType

T = TypeVar('T', bound='String')

class String(str):
    def slice(self: T, start: int, end: Union[int, None] = None) -> T:
        sliced_string = slice(self, start, end)
        return String(sliced_string)

    def split(self: T, separator = None) -> List:
        if bool(separator):
            string = self.__str__().split(separator)
            split_string = List(string)
            return split_string

        split_string =  List(self)
        return split_string

    @property
    def length(self: T):
        return len(self)

    def sub(self: T, regex: Union[str, RegEx], replacement: str) -> T:
        if type(regex).__name__ == 'str' or type(regex).__name__ == 'String':
            return String(RegEx.sub(regex, replacement, self.__str__()))
        else:
            return String(RegEx.sub(regex.pattern, replacement, self.__str__()))

    def rstrip(self: T) -> T:
        return String(self.__str__().rstrip())

    def match(self: T, regex: Union[str, RegEx], flag: FlagType = None) -> bool:
        if not regex:
            return False
        if type(regex).__name__ == 'str' or type(regex).__name__ == 'String':
            pattern = RegEx(regex, flag)
            return pattern.match(self.__str__())
        else:
            return regex.match(self.__str__())

    def upper(self: T) -> T:
        return String(self.__str__().upper())

    def lower(self: T) -> T:
        return String(self.__str__().lower())

    def starts_with(self: T, target: str, end: int = None) -> bool:
        if not end:
            return self.__str__().startswith(target)
        else:
            return self.__str__().startswith(target, 0, end)

    def findMatches(self: T, regex: Union[str, RegEx], flag: FlagType = None) -> Union[List, None]:
        if type(regex).__name__ == 'str'  or type(regex).__name__ == 'String':
            pattern = RegEx(regex, flag)
            matches = pattern.findall(self.__str__())
            if not matches:
                return None
            return List(matches)
        else:
            matches = regex.findall(self.__str__())
            if not matches:
                return None
            return List(matches)

    def trim(self: T) -> T:
        return String(self.__str__().strip())

    def search(self: T, term: str) -> int:
        return String(self.__str__().find(term))

    def substring(self: T, start: int, end: int = None) -> T:
        if not end:
            return String(self.__str__()[start:])
        return String(self.__str__()[start: end])
