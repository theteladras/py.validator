from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

passport_regex_by_country_code = {
  "AM": "^[A-Z]{2}\d{7}$", # ARMENIA
  "AR": "^[A-Z]{3}\d{6}$", # ARGENTINA
  "AT": "^[A-Z]\d{7}$", # AUSTRIA
  "AU": "^[A-Z]\d{7}$", # AUSTRALIA
  "BA": "^[A-Z]\d{7}$", # BOSNIA AND HERZEGOVINA,
  "BE": "^[A-Z]{2}\d{6}$", # BELGIUM
  "BG": "^\d{9}$", # BULGARIA
  "BR": "^[A-Z]{2}\d{6}$", # BRAZIL
  "BY": "^[A-Z]{2}\d{7}$", # BELARUS
  "CA": "^[A-Z]{2}\d{6}$", # CANADA
  "CH": "^[A-Z]\d{7}$", # SWITZERLAND
  "CN": "^G\d{8}$|^E(?![IO])[A-Z0-9]\d{7}$", # CHINA
  "CY": "^[A-Z](\d{6}|\d{8})$", # CYPRUS
  "CZ": "^\d{8}$", # CZECH REPUBLIC
  "DE": "^[CFGHJKLMNPRTVWXYZ0-9]{9}$", # GERMANY
  "DK": "^\d{9}$", # DENMARK
  "DZ": "^\d{9}$", # ALGERIA
  "EE": "^([A-Z]\d{7}|[A-Z]{2}\d{7})$",  # ESTONIA
  "ES": "^[A-Z0-9]{2}([A-Z0-9]?)\d{6}$", # SPAIN
  "FI": "^[A-Z]{2}\d{7}$", # FINLAND
  "FR": "^\d{2}[A-Z]{2}\d{5}$", # FRANCE
  "GB": "^\d{9}$", # UNITED KINGDOM
  "GR": "^[A-Z]{2}\d{7}$", # GREECE
  "HR": "^\d{9}$", # CROATIA
  "HU": "^[A-Z]{2}(\d{6}|\d{7})$", # HUNGARY
  "IE": "^[A-Z0-9]{2}\d{7}$", # IRELAND
  "IN": "^[A-Z]{1}-?\d{7}$", # INDIA
  "ID": "^[A-C]\d{7}$", # INDONESIA
  "IR": "^[A-Z]\d{8}$", # IRAN
  "IS": "^(A)\d{7}$", # ICELAND
  "IT": "^[A-Z0-9]{2}\d{7}$", # ITALY
  "JP": "^[A-Z]{2}\d{7}$", # JAPAN
  "KR": "^[MS]\d{8}$", # SOUTH KOREA, REPUBLIC OF KOREA
  "LT": "^[A-Z0-9]{8}$", # LITHUANIA
  "LU": "^[A-Z0-9]{8}$", # LUXEMBURG
  "LV": "^[A-Z0-9]{2}\d{7}$", # LATVIA
  "LY": "^[A-Z0-9]{8}$", # LIBYA
  "MT": "^\d{7}$", # MALTA
  "MZ": "^([A-Z]{2}\d{7})|(\d{2}[A-Z]{2}\d{5})$", # MOZAMBIQUE
  "MY": "^[AHK]\d{8}$", # MALAYSIA
  "NL": "^[A-Z]{2}[A-Z0-9]{6}\d$", # NETHERLANDS
  "PL": "^[A-Z]{2}\d{7}$", # POLAND
  "PT": "^[A-Z]\d{6}$", # PORTUGAL
  "RO": "^\d{8,9}$", # ROMANIA
  "RS": "^\d{9}$", # SERBIA,
  "RU": "^\d{9}$", # RUSSIAN FEDERATION
  "SE": "^\d{8}$", # SWEDEN
  "SL": "^(P)[A-Z]\d{7}$", # SLOVANIA
  "SK": "^[0-9A-Z]\d{7}$", # SLOVAKIA
  "TR": "^[A-Z]\d{8}$", # TURKEY
  "UA": "^[A-Z]{2}\d{6}$", # UKRAINE
  "US": "^\d{9}$", # UNITED STATES
}

def is_passport_number(input: str, country_code: str) -> bool:
    input = assert_string(input).sub(RegEx("\s", "g"), "").upper()

    is_valid_country = country_code in passport_regex_by_country_code

    if not is_valid_country:
        return False

    return input.match(passport_regex_by_country_code[country_code])
