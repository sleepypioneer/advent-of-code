from .challenge import get_product_of_possible_wins


def main():
    races = """Time:        53     71     78     80
Distance:   275   1181   1215   1524"""
    puzzle_input_one = get_product_of_possible_wins(races)
    print(f"Puzzle solution part 1: {puzzle_input_one}")


if __name__ == "__main__":
    main()
    # Puzzle solution part 1: 449820
