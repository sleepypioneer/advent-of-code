def matches_on_card(winning_numbers: list[int], card_numbers: list[int]) -> int:
    return len(set(winning_numbers).intersection(card_numbers))


def split_card(card: str) -> (list[int], list[int]):
    winning_numbers, card_numbers = (
        [value for value in card.split(":")[1].split("|")[0].split(" ") if len(value) > 0],
        [value for value in card.split(":")[1].split("|")[1].split(" ") if len(value) > 0],
    )
    return winning_numbers, card_numbers


def calculate_card_score(matches: int) -> int:
    if matches == 0:
        return 0
    score = 1
    for _ in range(1, matches):
        score = score * 2
    return score


def calculate_total_score(cards: str) -> int:
    total_score = 0

    cards = cards.split("\n")
    for card in cards:
        winning_numbers, card_numbers = split_card(card)
        matches = matches_on_card(winning_numbers, card_numbers)
        score = calculate_card_score(matches)
        total_score += score
    return total_score
