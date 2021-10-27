from utils.to_date import to_date, default

def is_before(input, date = default()):
    comparison = to_date(date)
    original = to_date(input)
    return bool(original and comparison and original < comparison)
