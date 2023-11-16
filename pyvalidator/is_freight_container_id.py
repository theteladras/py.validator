import re
from .utils.assert_string import assert_string

isISO6346Str = re.compile(r'^[A-Z]{3}((U[0-9]{7})|([J,Z][0-9]{6,7}))$')
isDigit = re.compile(r'^[0-9]$')

def is_freight_container_id(input):
    input = assert_string(input)
    input = input.upper()

    if not isISO6346Str.match(input):
        return False

    if len(input) == 11:
        _sum = 0
        for i in range(len(input) - 1):
            if not isDigit.match(input[i]):
                letterCode = ord(input[i]) - 55
                if letterCode < 11:
                    convertedCode = letterCode
                elif 11 <= letterCode <= 20:
                    convertedCode = 12 + (letterCode % 11)
                elif 21 <= letterCode <= 30:
                    convertedCode = 23 + (letterCode % 21)
                else:
                    convertedCode = 34 + (letterCode % 31)
                _sum += convertedCode * (2 ** i)
            else:
                _sum += int(input[i]) * (2 ** i)

        checkSumDigit = _sum % 11
        return int(input[-1]) == checkSumDigit

    return True
