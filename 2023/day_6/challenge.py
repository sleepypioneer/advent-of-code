def determine_possible_distances(total_time: int) -> list[int]:
    """
    Returns a list of possible distances for a given total time.
    This is determined by how long you hold versus how long you move.
    The speed you move is equal to the time you hold.
    So if you hold for 2 milliseconds, your speed will be 2 milliseconds.
    The distance you move is then equal to your speed times remaining time
    """
    possible_distances = []
    for hold in range(0, total_time + 1):
        time_to_move = total_time - hold
        distance = hold * time_to_move
        possible_distances.append(distance)
    return possible_distances


def determine_num_possible_wins(record_distance: int, possible_distances: list[int]) -> int:
    """
    Returns the number of possible wins for a given record distance.
    """
    return sum(1 for distance in possible_distances if distance > record_distance)


def get_time_distance_pairs(data_string: str) -> (list[int], list[int]):
    data_list = data_string.split("\n")
    time_list = [int(i) for i in data_list[0].split() if i.isdigit()]
    distance_list = [int(i) for i in data_list[1].split() if i.isdigit()]
    return time_list, distance_list


def get_product_of_possible_wins(data_string: str) -> int:
    total_times, distances = get_time_distance_pairs(data_string)
    product_possible_wins = 1
    for total_time, record_distance in zip(total_times, distances):
        possible_distances = determine_possible_distances(total_time)
        num_possible_wins = determine_num_possible_wins(record_distance, possible_distances)
        product_possible_wins *= num_possible_wins
    return product_possible_wins
