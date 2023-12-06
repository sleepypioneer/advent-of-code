from .challenge import get_seeds, get_locations, get_destination


test_map = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_get_destination_number():
    test_map = "test-map map:\n50 98 2\n52 50 48"
    test_cases = [
        (0, 0),
        (1, 1),
        (48, 48),
        (49, 49),
        (50, 52),
        (51, 53),
        (96, 98),
        (97, 99),
        (98, 50),
        (99, 51),
    ]

    for source, destination in test_cases:
        assert get_destination(test_map, source) == destination


def test_get_seeds():
    assert get_seeds(test_map) == [79, 14, 55, 13]


def test_get_locations():
    assert get_locations(test_map) == [82, 43, 86, 35]
