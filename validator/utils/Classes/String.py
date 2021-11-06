from typing import TypeVar, Union, Literal

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
        if type(regex).__name__ == 'str':
            return String(RegEx.sub(regex, replacement, self.__str__()))
        else:
            return String(RegEx.sub(regex.pattern, replacement, self.__str__()))

    def rstrip(self) -> T:
        return String(self.__str__().rstrip())

    def match(self: T, regex: Union[str, RegEx], flag: FlagType = None) -> bool:
        if not regex:
            return False
        if type(regex).__name__ == 'str':
            pattern = RegEx(regex, flag)
            return pattern.match(self.__str__())
        else:
            return regex.match(self.__str__())

    def upper(self) -> T:
        return String(self.__str__().upper())

    def lower(self) -> T:
        return String(self.__str__().lower())
