from .challenge import create_grid, find_numbers_touching_symbols


def main():
    with open("2023/day_3/schematic.txt", "r") as f:
        schematic = f.read()
    grid = create_grid(schematic)
    numbers_touching_symbols = find_numbers_touching_symbols(grid)
    puzzle_input_one = sum(numbers_touching_symbols)
    print(f"Puzzle solution part 1: {puzzle_input_one}")


if __name__ == "__main__":
    main()
    # Puzzle solution part 1: 533784
