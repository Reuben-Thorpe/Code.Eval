#!/usr/bin/env python3
# Reuben Thorpe (2016), CodeEval [Number Pairs v1.0]
from sys import argv
from itertools import combinations


def parse_problem(file_path):
    with open(file_path, "r") as in_file:
        for line in in_file:
            sequence, target = line.split(';')
            target = int(target)
            sequence = set(int(num) for num in sequence.split(','))
            yield([target, sequence])


if __name__ == "__main__":
    for problem in parse_problem(argv[1]):
        target, seq = problem

        result = sorted(sorted(pair) for pair in combinations(seq, 2)
                        if target == sum(pair))

        if not result:
            print("NULL")
        else:
            print(";".join("{},{}".format(*pair) for pair in result))



