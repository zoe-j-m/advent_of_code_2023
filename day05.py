from typing import List, Tuple, Dict
from utilities import file_handling


def break_up(lines: List[str], acc: List[str]) -> List[List[str]]:
    if len(lines) == 0:
        return [acc]
    if len(lines[0]) == 0:
        return [acc] + break_up(lines[1:], [])
    acc.append(lines[0])
    return break_up(lines[1:], acc)


def maplist_to_dict(maplist: List[str]) -> Dict[int, Tuple[int, int]]:
    result = {}
    for mapping in maplist[1:]:
        split_mapping = list(map(int, mapping.split()))
        map_from, map_to, count = split_mapping[1], split_mapping[0], split_mapping[2]
        result[map_from] = (map_from + count, map_to - map_from)
    return result


def parse_to_maps(lines: List[str]) -> Tuple[List[int], List[Dict[int, Tuple[int, int]]]]:
    seeds = list(map(int, lines[0].split()[1:]))
    maps = list(map(maplist_to_dict, break_up(lines[2:], [])))
    return seeds, maps


def part1(lines: List[str]) -> int:
    seeds, maps = parse_to_maps(lines)
    results = []
    for seed in seeds:
        current = seed
        for this_map in maps:
            lower_keys = [key for key in this_map.keys() if key <= current]
            if len(lower_keys) == 0:
                continue
            nearest_key = max(lower_keys)
            if this_map[nearest_key][0] >= current:
                current = current + this_map[nearest_key][1]
        results.append(current)
    return min(results)


def part2(lines: List[str]) -> int:
    seeds, maps = parse_to_maps(lines)

    current_ranges = []
    for i in range(0, len(seeds) // 2):
        current_ranges.append((seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1]-1))

    thing = 0
    for this_map in maps:
        thing += 1
        mapped = []
        for current in current_ranges:
            # f -- k --- t - v
            # k -- f -- t - v
            # k -- f -- v -- t
            covered_keys = [key for key, value in this_map.items() if
                            not(current [1] < key or value[0] < current[0])]
            covered_keys.sort()
            last = current
            for key in covered_keys:
                item = this_map[key]
                new_range = (max(current[0], key) + item[1], min(current[1], item[0]) + item[1])
                # 7 54072971
                # 5 3330762831
                # 4 4198021275
                if new_range[0] <= 4198021275 <= new_range[1]:
                    print('!!!!', thing, key, item, current, 4198021275 - item[1])

                mapped.append (new_range)
                if current[0] < key:
                    mapped.append((current[0], key - 1))
                if current[1] > item[0] + 1:
                    last = (item[0]+1, current[1])
                else:
                    last = []
                current = (max(current[0], key) + 1, current[1])
            if len(last) > 0:
                mapped.append(last)
            a = min(list(map(lambda x : x[0], mapped)))
        current_ranges = mapped

    return min(list(map(lambda x : x[0], current_ranges)))


if __name__ == "__main__":
    data = file_handling.input_as_lines("data/day05")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
