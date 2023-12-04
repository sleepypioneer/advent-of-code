################# GAME MAP ######################
# create a game map from the game text string   #
# by splitting the string into games and rounds #
#################################################


def get_games_map(game_text: str) -> dict:
    """
    returns a map of games, which is a map of rounds, which is a map of colors and their values
    example text = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    expected map = {
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
    }

    :param game_text: game text
    :type game_text: str
    :return: dict
    :rtype: dict
    """
    games_map = {}
    for game in game_text.splitlines():
        game_name, rounds_text = game.split(": ")
        game_name = game_name.strip().replace(" ", "_").lower()
        games_map[game_name] = []
        for round_text in rounds_text.split("; "):
            games_map[game_name.lower()].append(get_round_map(round_text))
    return games_map


def get_round_map(round_text: str) -> dict:
    """
    returns a map of colors and their values
    example text = "3 blue, 4 red"
    expected map = {
        "blue": 3,
        "red": 4,
    }

    :param round_text: round text
    :type round_text: str
    :return: dict
    :rtype: dict
    """
    round_map = {}
    for color_value in round_text.split(", "):
        value, color = color_value.split(" ")
        round_map[color.lower()] = int(value)
    return round_map


################# FIND POSSIBLE GAMES ######################
# Determine if games are possible with the available cubes #
# For a game to be possible, all rounds must be possible   #
# Take the number of the game as it's id ie game_1 = 1     #
############################################################


def possible_game(game: list[map], available_cubes: map) -> bool:
    """
    returns True if the game is possible, False otherwise
    :param game: game
    :type game: list[map]
    :param available_cubes: available cubes
    :type available_cubes: dict
    :return: True if the game is possible, False otherwise
    :rtype: bool
    """
    for round in game:
        for color in round.keys():
            if round[color] > available_cubes[color]:
                return False
    return True


def get_possible_games(games_map: dict, available_cubes: map) -> list[str]:
    """
    returns a list of possible games
    :param games_map: games map
    :type games_map: dict
    :param available_cubes: available cubes
    :type available_cubes: map
    :return: list[str]
    :rtype: list[str]
    """
    possible_games = []
    for game_name, game in games_map.items():
        if possible_game(game, available_cubes):
            possible_games.append(game_name)
    return possible_games


def get_possible_game_ids(possible_games: list[str]) -> list[int]:
    """
    returns a list of possible game ids
    :param possible_games: list of possible games
    :type possible_games: list
    :param available_cubes: available cubes
    :type available_cubes: map
    :return: list[int]
    :rtype: list[int]
    """
    possible_game_ids = []
    for game_name in possible_games:
        possible_game_ids.append(int(game_name.split("_")[1]))
    return possible_game_ids
