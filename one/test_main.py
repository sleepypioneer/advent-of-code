from .challenge import get_puzzle_input


EXAMPLE_CALIBRATION_BLOCK = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXPECTED_PUZZLE_INPUT = 142


def test_get_puzzle_input():
    puzzle_input = get_puzzle_input(EXAMPLE_CALIBRATION_BLOCK)
    assert puzzle_input == EXPECTED_PUZZLE_INPUT
