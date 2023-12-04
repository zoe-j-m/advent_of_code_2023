from typing import List, Optional, Tuple
from utilities import file_handling

def check(lines: List[str], from_col : int, to_col : int, row: int) -> bool:
    max_row = len(lines) - 1
    i_from, i_to = max(0, from_col - 1), min(len(lines[0]) - 1, to_col + 1)
    for i in range(i_from, i_to + 1):
        if row > 0:
            if lines[row - 1][i] != '.':
                return True
        if row < max_row:
            if lines[row + 1][i] != '.':
                 return True
        if (i == i_from and from_col !=0) or (i == i_to and to_col != len(lines[0])-1):
            if lines[row][i] != '.':
                return True
    return False


def check_pt2(lines: List[str], from_col : int, to_col : int, row: int) -> Optional[Tuple[int, int]]:
    max_row = len(lines) - 1
    i_from, i_to = max(0, from_col - 1), min(len(lines[0]) - 1, to_col + 1)
    for i in range(i_from, i_to + 1):
        if row > 0:
            if lines[row - 1][i] == '*':
                return (row-1, i)
        if row < max_row:
            if lines[row + 1][i] == '*':
                 return (row+1, i)
        if (i == i_from and from_col !=0) or (i == i_to and to_col != len(lines[0])-1):
            if lines[row][i] == '*':
                return (row, i)
    return None


def part1(lines: List[str]) -> int:
    total = 0
    start_col = 0
    for row, line in enumerate(lines):
        current = ''
        for col, char in enumerate(line):
            if char.isdigit():
                if len(current) == 0:
                    start_col = col
                current += char
            if len(current) > 0 and (not char.isdigit() or col == len(line) - 1):
                value = int(current)
                
                if check(lines, start_col, start_col + len(current) - 1, row):
                    print(value)
                    total += value
                current = ''
    return total


def part2(lines: List[str]) -> int:
    total = 0
    start_col = 0
    gears = {}
    for row, line in enumerate(lines):
        current = ''
        for col, char in enumerate(line):
            if char.isdigit():
                if len(current) == 0:
                    start_col = col
                current += char
            if len(current) > 0 and (not char.isdigit() or col == len(line) - 1):
                value = int(current)
                check_result = check_pt2(lines, start_col, start_col + len(current) - 1, row)
                if check_result:
                    if check_result in gears:
                        total += value * gears[check_result]
                    else:
                        gears[check_result] = value
                current = ''
    return total





if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day03")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
