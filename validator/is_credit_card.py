from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .is_number import is_number

credit_card = RegEx("^(?:4[0-9]{12}(?:[0-9]{3,6})?|5[1-5][0-9]{14}|(222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|6(?:011|5[0-9][0-9])[0-9]{12,15}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11}|6[27][0-9]{14}|^(81[0-9]{14,17}))$")

sanetization_pattern = RegEx("[- ]+", 'g')

def is_credit_card(input: str) -> bool:
    input = assert_string(input)

    sanitized = input.sub(sanetization_pattern, '')

    if not credit_card.match(sanitized):
        return False

    sum = 0
    should_double = False
    reversed_sanetized_input = sanitized[::-1]

    for digit in reversed_sanetized_input:
        if not is_number(digit):
            return False

        tmp_num = int(float(digit))

        if should_double:
            tmp_num = tmp_num * 2
            if tmp_num >= 10:
                sum += ((tmp_num % 10) + 1)
            else:
                sum += tmp_num
        else:
            sum += tmp_num
        should_double = not should_double

    return bool(sanitized if (sum % 10) == 0 else False)
