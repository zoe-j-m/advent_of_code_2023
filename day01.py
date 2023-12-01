from typing import List
from utilities import file_handling

DIGITS = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven': '7', 'eight': '8', 'nine' : '9', 'zero' : '0'}

def value_from_digits(digits: List[str]) -> int:
    return int(digits[0] + digits[-1])

def line_to_number(line: str) -> int:
    digits = [x for x in line if x.isdigit()]
    return value_from_digits(digits)

def replace_words_with_digits(line: str) -> List[str]:
    if len(line) == 0:
        return []
    for x in DIGITS.keys():
        if line.startswith(x):
            return [DIGITS[x]] + replace_words_with_digits(line[1:])
    if line[0].isdigit():
        return [line[0]] + replace_words_with_digits(line[1:])
    else:
        return replace_words_with_digits(line[1:])

def part1(lines: List[str]) -> int:
    return sum(list(map(line_to_number, lines)))


def part2(lines: List[str]) -> int:
    return sum(list(map(lambda x: value_from_digits(replace_words_with_digits(x)), lines)))


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day01")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
