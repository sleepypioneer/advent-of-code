from .challenge import (
    determine_possible_distances,
    determine_num_possible_wins,
    get_time_distance_pairs,
    get_product_of_possible_wins,
)


test_data = """Time:      7  15   30
Distance:  9  40  200"""


def test_determine_possible_distances():
    total_time = 7
    expected = [0, 6, 10, 12, 12, 10, 6, 0]
    actual = determine_possible_distances(total_time)
    assert actual == expected


def test_determine_num_possible_wins():
    record_distance = 9
    possible_distances = [0, 6, 10, 12, 12, 10, 6, 0]
    expected = 4
    actual = determine_num_possible_wins(record_distance, possible_distances)
    assert actual == expected


def test_get_time_distance_pairs():
    expected = ([7, 15, 30], [9, 40, 200])
    actual = get_time_distance_pairs(test_data)
    assert actual == expected


def test_get_product_of_possible_wins():
    expected = 288
    actual = get_product_of_possible_wins(test_data)
    assert actual == expected
