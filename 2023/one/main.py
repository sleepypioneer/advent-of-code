from .challenge import get_puzzle_input_challenge_one


def main():
    with open("2023/one/calibration_block.txt", "r") as f:
        calibration_block = f.read()
    puzzle_input = get_puzzle_input_challenge_one(calibration_block)
    print(f"Puzzle solution part 1: {puzzle_input}")


if __name__ == "__main__":
    main()
