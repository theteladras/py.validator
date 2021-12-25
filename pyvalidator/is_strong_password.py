from typing import TypedDict

from .utils.Classes.String import String
from .utils.assert_string import assert_string
from .utils.merge import merge

class _IsStrongPasswordOptions(TypedDict):
    min_length: int
    min_uppercase: int
    min_lowercase: int
    min_numbers: int
    min_symbols: int
    return_score: bool
    points_per_unique: int
    points_per_repeat: float
    points_for_containing_upper: int
    points_for_containing_lower: int
    points_for_containing_number: int
    points_for_containing_symbol: int

class _Analysis(TypedDict):
    length: int
    unique_chars: int
    uppercase_count: int
    lowercase_count: int
    number_count: int
    symbol_count: int

upper_case_regex = r"^[A-Z]$"
lower_case_regex = r"^[a-z]$"
number_regex = r"^[0-9]$"
symbol_regex = r"^[-#!$@%^&*()_+|~=`{}\[\]:\";'<>?,.\/ ]$"

default_options: _IsStrongPasswordOptions = {
  "min_length": 8,
  "min_uppercase": 1,
  "min_lowercase": 1,
  "min_numbers": 1,
  "min_symbols": 1,
  "return_score": False,
  "points_per_unique": 1,
  "points_per_repeat": 0.5,
  "points_for_containing_lower": 10,
  "points_for_containing_upper": 10,
  "points_for_containing_number": 10,
  "points_for_containing_symbol": 10,
}

def count_chars(pw: String):
    result = {}
    for char in pw:
        if char in result:
            result[char] += result[char] + 1
        else:
            result[char] = 1
    return result

def analyze_password(pw: String) -> _Analysis:
    char_map = count_chars(pw)
    analysis: _Analysis = {
        "length": pw.length,
        "unique_chars": len([*char_map]),
        "uppercase_count": 0,
        "lowercase_count": 0,
        "number_count": 0,
        "symbol_count": 0,
    }
    for char in [*char_map]:
        char = String(char)
        if char.match(upper_case_regex):
            analysis["uppercase_count"] += char_map[char]
        elif char.match(lower_case_regex):
            analysis["lowercase_count"] += char_map[char]
        elif char.match(number_regex):
            analysis["number_count"] += char_map[char]
        elif char.match(symbol_regex):
            analysis["symbol_count"] += char_map[char]
    return analysis

def score_password(analysis: _Analysis, options: _IsStrongPasswordOptions):
    points = 0
    points += analysis["unique_chars"] * options["points_per_unique"]
    points += (analysis["length"] - analysis["unique_chars"]) * options["points_per_unique"]
    if analysis["uppercase_count"] > 0:
        points += options["points_for_containing_upper"]
    if analysis["lowercase_count"] > 0:
        points += options["points_for_containing_lower"]
    if analysis["number_count"] > 0:
        points += options["points_for_containing_number"]
    if analysis["symbol_count"] > 0:
        points += options["points_for_containing_symbol"]
    return points

def is_strong_password(input: str, options: _IsStrongPasswordOptions = {}) -> bool:
    input = assert_string(input)
    options = merge(options, default_options)

    analysis = analyze_password(input)
    if options["return_score"]:
        return score_password(analysis, options)
    return (
        analysis["length"] >= options["min_length"] and
        analysis["uppercase_count"] >= options["min_uppercase"] and
        analysis["lowercase_count"] >= options["min_lowercase"] and
        analysis["number_count"] >= options["min_numbers"] and
        analysis["symbol_count"] >= options["min_symbols"]
    )
