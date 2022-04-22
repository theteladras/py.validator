def includes(list, val):
    return val in list


def includesNot(list, val):
    return val not in list


def includesSome(list, listVal):
    for item in listVal:
        if item in list:
            return True
    return False
