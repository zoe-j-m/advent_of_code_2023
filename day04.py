import re
from typing import List, Tuple, Set

from utilities import file_handling

REGEX = r'Card +(\d+): +((?:\d+ *)+)\| +((?:\d+ *)+)'


def parse_to_card(line: str) -> Tuple[int, Set[int], Set[int]]:
    groups = re.search(REGEX, line).groups()
    card_id = int(groups[0])
    winning = set(map(int, groups[1].split()))
    numbers = set(map(int, groups[2].split()))
    return card_id, winning, numbers


def score_card(winning: Set[int], numbers: Set[int]) -> int:
    matches = winning.intersection(numbers)
    if len(matches) == 0:
        return 0
    else:
        return 2 ** (len(matches)-1)


def part1(lines: List[str]) -> int:
    cards = list(map(parse_to_card, lines))
    scores = list(map(lambda x: score_card(x[1], x[2]), cards))
    return sum(scores)


def part2(lines: List[str]) -> int:
    cards_list = list(map(parse_to_card, lines))
    card_count = len(cards_list)
    scores_dict = dict([(card[0], 1) for card in cards_list])
    for card_id, winning, numbers in cards_list:
        score = len(winning.intersection(numbers))
        for i in range(card_id + 1, min(card_id + score + 1, card_count + 1)):
            assert score > 0
            scores_dict[i] += scores_dict[card_id]
    return sum(scores_dict.values())


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day04")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
