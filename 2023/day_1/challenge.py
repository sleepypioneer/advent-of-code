def get_puzzle_input_challenge_one(calibration_block):
    return get_puzzle_input_challenge(calibration_block)


def get_puzzle_input_challenge_two(calibration_block):
    return get_puzzle_input_challenge(calibration_block, include_char_digits=True)


def get_puzzle_input_challenge(calibration_block, include_char_digits=False):
    """
    returns the puzzle input, which is the sum of the line calibration values

    :param calibration_block: calibration block
    :type calibration_block: str
    :return: puzzle input
    :rtype: int
    """
    line_calibration_values = [
        get_line_calibration_value(line, include_char_digits)
        for line in calibration_block.splitlines()
    ]
    # Return the sum of the line calibration values to get the puzzle input
    return sum(line_calibration_values)


def get_line_calibration_value(line, include_char=False):
    """
    returns the line calibration value, which is the sum of the first digit and the last digit

    :param line: line
    :type line: str
    :return: line calibration value
    :rtype: int
    """
    first_digit = find_digit(line, DIGITS, include_char)

    # reverse the line to find the last digit
    reversed_line = line[::-1]
    last_digit = find_digit(reversed_line, REVERSED_DIGITS, include_char)

    return int(f"{first_digit}{last_digit}")


def find_digit(line: str, digits: map, include_chars=False):
    for idx, char in enumerate(line):
        digit = 0
        if char.isdigit():
            digit = char
        elif include_chars:
            digit = find_digit_as_char(line[idx:], digits)
        if digit != 0:
            break
    return digit


def find_digit_as_char(line: str, digits: map):
    for digit in digits.keys():
        if len(line) > len(digit) and all(
            # check if all the digit's characters appear in order
            [line[i] == digit[i] for i in range(0, len(digit), 1)]
        ):
            return digits[digit]
    # no digit found
    return 0


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

REVERSED_DIGITS = {
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}
