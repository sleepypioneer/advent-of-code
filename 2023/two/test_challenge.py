from .challenge import (
    get_games_map,
    possible_game,
    get_possible_games,
    get_possible_game_ids,
)


GAMES_MAP = {
    "game_1": [
        {
            "blue": 3,
            "red": 4,
        },
        {
            "green": 2,
            "blue": 6,
            "red": 1,
        },
        {
            "green": 2,
        },
    ],
    "game_2": [
        {
            "blue": 1,
            "green": 2,
        },
        {
            "green": 3,
            "blue": 4,
            "red": 6,
        },
        {
            "green": 1,
            "blue": 1,
        },
    ],
}


def test_get_games_map():
    games_text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 6 red; 1 green, 1 blue
"""
    games_map = get_games_map(games_text)
    assert games_map.keys() == GAMES_MAP.keys()


def test_possible_game():
    available_cubes = {"blue": 6, "green": 6, "red": 6}
    assert possible_game(GAMES_MAP["game_1"], available_cubes) is True


def test_possible_game_fail():
    available_cubes = {"blue": 4, "green": 4, "red": 4}
    assert possible_game(GAMES_MAP["game_1"], available_cubes) is False


def test_get_possible_games():
    available_cubes = {"blue": 6, "green": 4, "red": 4}
    assert get_possible_games(GAMES_MAP, available_cubes) == ["game_1"]


def test_get_possible_games_ids():
    possible_games = ["game_1", "game_2"]
    assert get_possible_game_ids(possible_games) == [1, 2]


def test_challenge_one():
    games_text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    available_cubes = {"blue": 14, "green": 13, "red": 12}
    games_map = get_games_map(games_text)
    possible_games = get_possible_games(games_map, available_cubes)
    possible_games_ids = get_possible_game_ids(possible_games)
    assert sum(possible_games_ids) == 8
