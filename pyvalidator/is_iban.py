from typing import TypedDict

from .utils.assert_string import assert_string
from .utils.merge import merge


class IsIbanOptions(TypedDict):
    insensitive: bool


default_options: IsIbanOptions = {
    "insensitive": False,
}

iban_patterns = {
    "AD": r"^AD\d{10}[A-Z0-9]{12}$",
    "AE": r"^AE\d{21}$",
    "AL": r"^AL\d{10}[A-Z0-9]{16}$",
    "AT": r"^AT\d{18}$",
    "AZ": r"^AZ\d{2}[A-Z]{4}[A-Z0-9]{20}$",
    "BA": r"^BA\d{18}$",
    "BE": r"^BE\d{14}$",
    "BG": r"^BG\d{2}[A-Z]{4}\d{6}[A-Z0-9]{8}$",
    "BH": r"^BH\d{2}[A-Z]{4}[A-Z0-9]{14}$",
    "BR": r"^BR\d{25}[A-Z]{1}[A-Z0-9]{1}$",
    "BY": r"^BY\d{2}[A-Z0-9]{4}\d{4}[A-Z0-9]{16}$",
    "CH": r"^CH\d{7}[A-Z0-9]{12}$",
    "CR": r"^CR\d{20}$",
    "CY": r"^CY\d{10}[A-Z0-9]{16}$",
    "CZ": r"^CZ\d{22}$",
    "DE": r"^DE\d{20}$",
    "DK": r"^DK\d{16}$",
    "DO": r"^DO\d{2}[A-Z0-9]{4}\d{20}$",
    "EE": r"^EE\d{18}$",
    "EG": r"^EG\d{27}$",
    "ES": r"^ES\d{22}$",
    "FI": r"^FI\d{16}$",
    "FO": r"^FO\d{16}$",
    "FR": r"^FR\d{12}[A-Z0-9]{11}\d{2}$",
    "GB": r"^GB\d{2}[A-Z]{4}\d{14}$",
    "GE": r"^GE\d{2}[A-Z]{2}\d{16}$",
    "GI": r"^GI\d{2}[A-Z]{4}[A-Z0-9]{15}$",
    "GL": r"^GL\d{16}$",
    "GR": r"^GR\d{9}[A-Z0-9]{16}$",
    "GT": r"^GT\d{2}[A-Z0-9]{24}$",
    "HR": r"^HR\d{19}$",
    "HU": r"^HU\d{26}$",
    "IE": r"^IE\d{2}[A-Z]{4}\d{14}$",
    "IL": r"^IL\d{21}$",
    "IQ": r"^IQ\d{2}[A-Z]{4}\d{15}$",
    "IS": r"^IS\d{24}$",
    "IT": r"^IT\d{2}[A-Z]{1}\d{10}[A-Z0-9]{12}$",
    "JO": r"^JO\d{2}[A-Z]{4}\d{4}[A-Z0-9]{18}$",
    "KW": r"^KW\d{2}[A-Z]{4}[A-Z0-9]{22}$",
    "KZ": r"^KZ\d{5}[A-Z0-9]{13}$",
    "LB": r"^LB\d{6}[A-Z0-9]{20}$",
    "LC": r"^LC\d{2}[A-Z]{4}[A-Z0-9]{24}$",
    "LI": r"^LI\d{7}[A-Z0-9]{12}$",
    "LT": r"^LT\d{18}$",
    "LU": r"^LU\d{5}[A-Z0-9]{13}$",
    "LV": r"^LV\d{2}[A-Z]{4}[A-Z0-9]{13}$",
    "MC": r"^MC\d{12}[A-Z0-9]{11}\d{2}$",
    "MD": r"^MD\d{2}[A-Z0-9]{20}$",
    "ME": r"^ME\d{20}$",
    "MK": r"^MK\d{5}[A-Z0-9]{10}\d{2}$",
    "MR": r"^MR\d{25}$",
    "MT": r"^MT\d{2}[A-Z]{4}\d{5}[A-Z0-9]{18}$",
    "MU": r"^MU\d{2}[A-Z]{4}\d{19}[A-Z]{3}$",
    "NL": r"^NL\d{2}[A-Z]{4}\d{10}$",
    "NO": r"^NO\d{13}$",
    "PK": r"^PK\d{2}[A-Z]{4}[A-Z0-9]{16}$",
    "PL": r"^PL\d{26}$",
    "PS": r"^PS\d{2}[A-Z]{4}[A-Z0-9]{21}$",
    "PT": r"^PT\d{23}$",
    "QA": r"^QA\d{2}[A-Z]{4}[A-Z0-9]{21}$",
    "RO": r"^RO\d{2}[A-Z]{4}[A-Z0-9]{16}$",
    "RS": r"^RS\d{20}$",
    "SA": r"^SA\d{4}[A-Z0-9]{18}$",
    "SC": r"^SC\d{2}[A-Z]{4}\d{20}[A-Z]{3}$",
    "SE": r"^SE\d{22}$",
    "SI": r"^SI\d{17}$",
    "SK": r"^SK\d{22}$",
    "SM": r"^SM\d{2}[A-Z]{1}\d{10}[A-Z0-9]{12}$",
    "ST": r"^ST\d{23}$",
    "SV": r"^SV\d{2}[A-Z]{4}\d{20}$",
    "TL": r"^TL\d{21}$",
    "TN": r"^TN\d{22}$",
    "TR": r"^TR\d{8}[A-Z0-9]{16}$",
    "UA": r"^UA\d{8}[A-Z0-9]{19}$",
    "VA": r"^VA\d{20}$",
    "VG": r"^VG\d{2}[A-Z]{4}\d{16}$",
}


def is_iban(input: str, country_code: str = None, options: IsIbanOptions = {}) -> bool:
    input = assert_string(input.replace(' ', '')).trim()

    options = merge(options, default_options)

    if options["insensitive"]:
        input = input.upper()
        if country_code:
            country_code = country_code.upper()

    if not input:
        return False

    country_code_from_input = input[:2]

    if not country_code:
        country_code = country_code_from_input
    else:
        country_code = country_code.upper()
        if country_code_from_input != country_code:
            input = input.prefix(country_code)

    if country_code not in iban_patterns:
        return False

    return input.match(iban_patterns[country_code])
