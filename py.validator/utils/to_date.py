import datetime
from .assert_string import assert_string

def __parse_date(str):
    try:
        return datetime.datetime.fromisoformat(str)
    except:
        return None

def to_date(str):
    assert_string(str)
    date = __parse_date(str)
    return date if bool(date) else None
    
def default():
    return datetime.datetime.now().isoformat()
