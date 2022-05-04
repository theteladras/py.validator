import datetime

import timestring

from .assert_string import assert_string


def __parse_date(input: str):
    try:
        return timestring.Date(input).date
    except:
        return None


def to_date(input: str):
    assert_string(input)
    date = __parse_date(input)
    return date if bool(date) else None


def default_date_string():
    return datetime.datetime.now().isoformat()
