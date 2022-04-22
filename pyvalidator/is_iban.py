from typing import TypedDict

from .utils.assert_string import assert_string
from .utils.merge import merge


class IsIbanOptions(TypedDict):
    insensitive: bool


default_options: IsIbanOptions = {
    "insensitive": False,
}

iban_patterns = {
    "AD": "^AD\\d{10}[A-Z0-9]{12}$",
    "AE": "^AE\\d{21}$",
    "AL": "^AL\\d{10}[A-Z0-9]{16}$",
    "AT": "^AT\\d{18}$",
    "AZ": "^AZ\\d{2}[A-Z]{4}[A-Z0-9]{20}$",
    "BA": "^BA\\d{18}$",
    "BE": "^BE\\d{14}$",
    "BG": "^BG\\d{2}[A-Z]{4}\\d{6}[A-Z0-9]{8}$",
    "BH": "^BH\\d{2}[A-Z]{4}[A-Z0-9]{14}$",
    "BR": "^BR\\d{25}[A-Z]{1}[A-Z0-9]{1}$",
    "BY": "^BY\\d{2}[A-Z0-9]{4}\\d{4}[A-Z0-9]{16}$",
    "CH": "^CH\\d{7}[A-Z0-9]{12}$",
    "CR": "^CR\\d{20}$",
    "CY": "^CY\\d{10}[A-Z0-9]{16}$",
    "CZ": "^CZ\\d{22}$",
    "DE": "^DE\\d{20}$",
    "DK": "^DK\\d{16}$",
    "DO": "^DO\\d{2}[A-Z0-9]{4}\\d{20}$",
    "EE": "^EE\\d{18}$",
    "EG": "^EG\\d{27}$",
    "ES": "^ES\\d{22}$",
    "FI": "^FI\\d{16}$",
    "FO": "^FO\\d{16}$",
    "FR": "^FR\\d{12}[A-Z0-9]{11}\\d{2}$",
    "GB": "^GB\\d{2}[A-Z]{4}\\d{14}$",
    "GE": "^GE\\d{2}[A-Z]{2}\\d{16}$",
    "GI": "^GI\\d{2}[A-Z]{4}[A-Z0-9]{15}$",
    "GL": "^GL\\d{16}$",
    "GR": "^GR\\d{9}[A-Z0-9]{16}$",
    "GT": "^GT\\d{2}[A-Z0-9]{24}$",
    "HR": "^HR\\d{19}$",
    "HU": "^HU\\d{26}$",
    "IE": "^IE\\d{2}[A-Z]{4}\\d{14}$",
    "IL": "^IL\\d{21}$",
    "IQ": "^IQ\\d{2}[A-Z]{4}\\d{15}$",
    "IS": "^IS\\d{24}$",
    "IT": "^IT\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}$",
    "JO": "^JO\\d{2}[A-Z]{4}\\d{4}[A-Z0-9]{18}$",
    "KW": "^KW\\d{2}[A-Z]{4}[A-Z0-9]{22}$",
    "KZ": "^KZ\\d{5}[A-Z0-9]{13}$",
    "LB": "^LB\\d{6}[A-Z0-9]{20}$",
    "LC": "^LC\\d{2}[A-Z]{4}[A-Z0-9]{24}$",
    "LI": "^LI\\d{7}[A-Z0-9]{12}$",
    "LT": "^LT\\d{18}$",
    "LU": "^LU\\d{5}[A-Z0-9]{13}$",
    "LV": "^LV\\d{2}[A-Z]{4}[A-Z0-9]{13}$",
    "MC": "^MC\\d{12}[A-Z0-9]{11}\\d{2}$",
    "MD": "^MD\\d{2}[A-Z0-9]{20}$",
    "ME": "^ME\\d{20}$",
    "MK": "^MK\\d{5}[A-Z0-9]{10}\\d{2}$",
    "MR": "^MR\\d{25}$",
    "MT": "^MT\\d{2}[A-Z]{4}\\d{5}[A-Z0-9]{18}$",
    "MU": "^MU\\d{2}[A-Z]{4}\\d{19}[A-Z]{3}$",
    "NL": "^NL\\d{2}[A-Z]{4}\\d{10}$",
    "NO": "^NO\\d{13}$",
    "PK": "^PK\\d{2}[A-Z]{4}[A-Z0-9]{16}$",
    "PL": "^PL\\d{26}$",
    "PS": "^PS\\d{2}[A-Z]{4}[A-Z0-9]{21}$",
    "PT": "^PT\\d{23}$",
    "QA": "^QA\\d{2}[A-Z]{4}[A-Z0-9]{21}$",
    "RO": "^RO\\d{2}[A-Z]{4}[A-Z0-9]{16}$",
    "RS": "^RS\\d{20}$",
    "SA": "^SA\\d{4}[A-Z0-9]{18}$",
    "SC": "^SC\\d{2}[A-Z]{4}\\d{20}[A-Z]{3}$",
    "SE": "^SE\\d{22}$",
    "SI": "^SI\\d{17}$",
    "SK": "^SK\\d{22}$",
    "SM": "^SM\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}$",
    "ST": "^ST\\d{23}$",
    "SV": "^SV\\d{2}[A-Z]{4}\\d{20}$",
    "TL": "^TL\\d{21}$",
    "TN": "^TN\\d{22}$",
    "TR": "^TR\\d{8}[A-Z0-9]{16}$",
    "UA": "^UA\\d{8}[A-Z0-9]{19}$",
    "VA": "^VA\\d{20}$",
    "VG": "^VG\\d{2}[A-Z]{4}\\d{16}$",
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
