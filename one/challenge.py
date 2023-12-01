def get_puzzle_input(calibration_block):
    """
    returns the puzzle input, which is the sum of the line calibration values

    :param calibration_block: calibration block
    :type calibration_block: str
    :return: puzzle input
    :rtype: int
    """
    line_calibration_values = [
        get_line_calibration_value(line) for line in calibration_block.splitlines()
    ]
    # Return the sum of the line calibration values to get the puzzle input
    return sum(line_calibration_values)


def get_line_calibration_value(line):
    """
    returns the line calibration value, which is the sum of the first digit and the last digit

    :param line: line
    :type line: str
    :return: line calibration value
    :rtype: int
    """
    first_digit = 0
    last_digit = 0
    # find the first digit per line
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    # find the last digit per line
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    # combine the first digit and the last digit to form calibration value
    return int(f"{first_digit}{last_digit}")
