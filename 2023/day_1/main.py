from .challenge import get_puzzle_input_challenge


def main():
    with open("2023/day_1/calibration_block.txt", "r") as f:
        calibration_block = f.read()
    puzzle_input_one = get_puzzle_input_challenge(calibration_block)
    print(f"Puzzle solution part 1: {puzzle_input_one}")

    puzzle_input_two = get_puzzle_input_challenge(
        calibration_block, include_char_digits=True
    )
    print(f"Puzzle solution part 2: {puzzle_input_two}")


if __name__ == "__main__":
    main()
    # Puzzle solution part 1: 54573
    # Puzzle solution part 2: 54591
