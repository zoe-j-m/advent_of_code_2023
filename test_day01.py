from day01 import part1, part2, replace_words_with_digits

test_lines = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''.split("\n")

test_lines2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.split("\n")

def test_part1():
    assert part1(test_lines) == 142

def test_replace_words():
    assert replace_words_with_digits('1two3four') == ['1','2','3','4']

def test_part2():
    assert part2(test_lines2) == 281
