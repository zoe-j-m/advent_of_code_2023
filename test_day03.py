from day03 import part1, part2

test_lines = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split("\n")

def test_part1():
    assert part1(test_lines) == 4361

def test_part2():
    assert part2(test_lines) == 467835
