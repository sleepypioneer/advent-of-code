from .challenge import get_games_map, get_possible_games, get_possible_game_ids


def main():
    with open("2023/two/games.txt", "r") as f:
        games_text = f.read()
    games_map = get_games_map(games_text)
    available_cubes = {"blue": 14, "green": 13, "red": 12}

    possible_games = get_possible_games(games_map, available_cubes)
    possible_games_ids = get_possible_game_ids(possible_games)

    # puzzle solution is the sum of all possible game ids
    puzzle_input_one = sum(possible_games_ids)

    print(f"Puzzle solution part 1: {puzzle_input_one}")


if __name__ == "__main__":
    main()
    # Puzzle solution part 1: 2207
