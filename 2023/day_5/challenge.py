def get_seeds(seed_map: str) -> list:
    return [int(value) for value in seed_map.split(":")[1].strip().split() if value.isdigit()]


def get_destination(map_string: str, source: int) -> int:
    for line in map_string.splitlines():
        if line[0].isalpha():
            # ignore the map name
            continue
        else:
            # get the three values from that row
            numbers = [int(value) for value in line.split() if value.isdigit()]
            if len(numbers) != 3:
                raise ValueError("Invalid line in map string")
            destination_start, source_start, _range = numbers
        # check if source value falls in the source range
        # and return destination
        if source_start <= source < source_start + _range:
            return destination_start + (source - source_start)
    # if no destination is found then it is the same as the source
    return source


def get_locations(maps: str) -> int:
    maps = maps.split("\n\n")

    seeds = get_seeds(maps[0])
    locations = []

    for seed in seeds:
        soil = get_destination(maps[1], seed)
        fertilizer = get_destination(maps[2], soil)
        water = get_destination(maps[3], fertilizer)
        light = get_destination(maps[4], water)
        temperature = get_destination(maps[5], light)
        humidity = get_destination(maps[6], temperature)
        location = get_destination(maps[7], humidity)
        locations.append(location)

    return locations
