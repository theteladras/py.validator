def slice(val, start, end):
    return val[start:end]

def slice_and_upper_case(val, start, end):
    sliced = slice(val, start, end)
    return sliced.upper()

def slice_and_lower_case(val, start, end):
    sliced = slice(val, start, end)
    return sliced.lower()
