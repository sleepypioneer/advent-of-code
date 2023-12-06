from .challenge import calculate_total_score


def main():
    """
    Runs the day 4 challenge.
    """
    with open("2023/day_4/scratch_cards.txt") as f:
        cards = f.read()
    puzzle_input_one = calculate_total_score(cards)
    print(f"Puzzle solution part 1: {puzzle_input_one}")


if __name__ == "__main__":
    main()
    # Puzzle solution part 1: 449820
