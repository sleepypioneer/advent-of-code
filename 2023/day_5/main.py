import timeit

from .challenge import get_locations


def main():
    start_time = timeit.default_timer()
    with open("2023/day_5/almanac.txt", "r") as f:
        maps = f.read()
    locations = get_locations(maps)
    puzzle_input_one = min(locations)
    print(f"Puzzle solution part 1: {puzzle_input_one}")
    print(f"Elapsed time: {timeit.default_timer()-start_time}")


if __name__ == "__main__":
    main()
    # Puzzle solution part 1: 525792406
