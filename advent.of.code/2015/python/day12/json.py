import re
import json

PARSE = r"(-?\d+)"


def part1(fileName):
    data = re.compile(PARSE).findall(open(fileName, 'r').read())
    print("\nPart 1 = ", sum((int(i) for i in data)))


def part2(fileName):
    data = json.loads(open(fileName, 'r').read())
    print("Part 2 = ", sum_numbers(data), "\n")


def sum_numbers(obj):
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(map(sum_numbers, obj.values()))

    elif isinstance(obj, list):
        return sum(map(sum_numbers, obj))

    elif isinstance(obj, int):
        return obj

    return 0


if __name__ == '__main__':
    part1('input.txt')
    part2('input.txt')
