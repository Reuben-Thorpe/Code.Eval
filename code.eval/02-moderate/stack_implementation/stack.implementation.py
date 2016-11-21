#!/usr/bin/env python3
# Reuben Thorpe (2016), CodeEval [Stack Implementation v1.0]
from sys import argv


def parse_problem(file_path):
    with open(file_path) as in_file:
        for line in in_file:
            yield(line.strip().split())


if __name__ == "__main__":
    for problem in parse_problem(argv[1]):
        print(" ".join(problem[::-2]))
