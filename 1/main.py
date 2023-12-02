from data import document

digit_map = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}


# String -> String or None
# return number representation of "one, two, three, four, five, six, seven, eight, or nine" starting from the beginning (ignore trailing characters)

def get_digit(str):
    sub_str = ''

    if str[0].isdigit():
        return str[0]

    for s in str:
        sub_str += s
        if sub_str in digit_map:
            return digit_map[sub_str]

    return None


assert get_digit('one1nine') == '1'
assert get_digit('two1nine') == '2'
assert get_digit('three1nine') == '3'
assert get_digit('four1nine') == '4'
assert get_digit('five1nine') == '5'
assert get_digit('six1nine') == '6'
assert get_digit('seven1nine') == '7'
assert get_digit('eight1nine') == '8'
assert get_digit('nine1nine') == '9'

# String -> Number
# combine the first and last number in the string
def decode(s):
    first_digit = None
    last_digit = None

    for i, char in enumerate(s):
        digit = get_digit(s[i: len(s)])

        if digit:
            if first_digit is None:
                first_digit = digit

            last_digit = digit

    # Combine the first and last digits
    if first_digit is None and last_digit is None:
        return 0

    return int(first_digit + last_digit)


assert decode('1abc2') == 12
assert decode('treb7uchet') == 77
assert decode('two1nine') == 29
assert decode('eightwothree') == 83
assert decode('abcone2threexyz') == 13
assert decode('xtwone3four') == 24
assert decode('4nineeightseven2') == 42
assert decode('zoneight234') == 14
assert decode('7pqrstsixteen') == 76


# ListOfString -> Number
# Decode each string and add them together
# NOTE: to decode a string, combine the first and last digit

def decode_calibration_document(doc):
    total = 0

    for s in doc:
        total += decode(str(s))

    return total


if __name__ == '__main__':
    print(decode_calibration_document(document))
