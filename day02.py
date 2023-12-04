from typing import List, Dict, Tuple
from utilities import file_handling
import re

REGEX_1 = r'Game (\d*): (.*)'
REGEX_2 = r'([^;]*)(?:; )?'
REGEX_3 = r'(?:(\d+) (\w+))'

def parse_to_games(line: str) -> Tuple[int, Dict[str, List[int]]]:
    game = re.search(REGEX_1, line).groups()
    rounds = re.findall(REGEX_2, game[1])
    colours = {}
    for round in rounds:
        pulls = re.findall(REGEX_3, round)
        for pull in pulls:
            colour = pull[1]
            number = int(pull[0])
            if colour in colours:
                colours[colour].append(number)
            else:
                colours[colour] = [number]
    return (int(game[0]), colours)
    
def part1_check(colour: str, pulls: Dict[str, List[int]], limit: int) -> bool:
    if colour not in pulls:
        return True
    for pull in pulls[colour]:
        if pull > limit:
            return False
    return True


def part1(lines: List[str]) -> int:
    games = list(map(parse_to_games,lines))
    filtered_ids = [game[0] for game in games if part1_check('red', game[1], 12) and part1_check('green', game[1], 13) and part1_check('blue', game[1], 14)]
    return sum(filtered_ids)


def part2(lines: List[str]) -> int:
    games = list(map(parse_to_games,lines))
    result = 0
    for id, game in games:
        result += max(game['red']) * max(game['blue'])  * max(game['green'])
    return result


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day02")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
