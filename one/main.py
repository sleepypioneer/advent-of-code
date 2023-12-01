from .challenge import get_puzzle_input


def main():
    with open("one/calibration_block.txt", "r") as f:
        calibration_block = f.read()
    puzzle_input = get_puzzle_input(calibration_block)
    print(f"Puzzle solution part 1: {puzzle_input}")


if __name__ == "__main__":
    main()
