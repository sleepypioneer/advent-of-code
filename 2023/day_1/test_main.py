from .challenge import (
    get_puzzle_input_challenge,
    get_line_calibration_value,
)


def test_get_puzzle_input_challenge_one():
    test_calibration_block = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
    expected_puzzle_input = 142

    assert get_puzzle_input_challenge(test_calibration_block) == expected_puzzle_input


def test_get_line_calibration_value():
    for line, value in zip(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], [12, 38, 15, 77]):
        assert get_line_calibration_value(line) == value


def test_get_puzzle_input_challenge_two():
    test_calibration_block = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""
    expected_puzzle_input = 281

    assert (
        get_puzzle_input_challenge(test_calibration_block, include_char_digits=True)
        == expected_puzzle_input
    )


def test_get_line_calibration_value_include_chars():
    for line, value in zip(
        [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "fiveeight2zxjpzffvdsevenjhjvjfiveonenine",
            "7576threesix",
            "mkdvknghvsgzrbbjqngbsqeight6mjxfivenineq",
            "one6fourrrrtkkjvr",
            "8twoone54sixvmlcjdnrgnqbmlrvdtnh",
            "7b",
            "eight0dhfeightfourght",
            "7pqrstsixteen",
        ],
        [29, 83, 13, 24, 42, 14, 59, 76, 89, 14, 86, 77, 84, 76],
    ):
        assert get_line_calibration_value(line, include_char=True) == value
