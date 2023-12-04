from typing import List, Dict, Tuple
from utilities import file_handling
import re

REGEX_1 = r'Game (\d*): (.*)'
REGEX_2 = r'([^;]*)(?:; )?'
REGEX_3 = r'(?:(\d+) (\w+))'

def parse_to_groups(line: str) -> Tuple[int, Dict[str, List[int]]]:
    print(line)
    capture_groups = re.search(REGEX_1, line).groups()
    rounds = re.findall(REGEX_2, capture_groups[1])
    thing = {}
    for round in rounds:
        pulls = re.findall(REGEX_3, round)
        for pull in pulls:
            colour = pull[1]
            number = int(pull[0])
            if colour in thing:
                thing[colour].append(number)
            else:
                thing[colour] = [number]
    return (int(capture_groups[0]), thing)
    
def part1_check(colour: str, pulls: Dict[str, List[int]], limit: int) -> bool:
    if colour not in pulls:
        return True
    for pull in pulls[colour]:
        if pull > limit:
            return False
    return True


def part1(lines: List[str]) -> int:
    groups = list(map(parse_to_groups,lines))
    filtered_ids = [group[0] for group in groups if part1_check('red', group[1], 12) and part1_check('green', group[1], 13) and part1_check('blue', group[1], 14)]
    return sum(filtered_ids)


def part2(lines: List[str]) -> int:
    groups = list(map(parse_to_groups,lines))
    result = 0
    for id, group in groups:
        result += max(group['red']) * max(group['blue'])  * max(group['green'])
    return result


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day02")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
