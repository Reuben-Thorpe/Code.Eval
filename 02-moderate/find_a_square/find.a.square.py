# Reuben Thorpe (2016), CodeEval [Find A Square v1.0]
from math import sqrt
from sys import argv
from ast import literal_eval
from itertools import combinations


def parse_problem(file_path):
    with open(argv[1], "r") as in_file:
        for line in in_file:
            yield(literal_eval(line.strip()))


def is_square(problem):
    distinct_distances = set()

    for (x1, y1), (x2, y2) in combinations(problem, 2):
        distinct_distances.add(sqrt((x2 - x1)**2 + (y2 - y1)**2))

        if len(distinct_distances) > 2:
            return(False)

    return(len(distinct_distances) == 2)


if __name__ == "__main__":
    for problem in parse_problem(argv[1]):
        if is_square(problem):
            print("true")
        else:
            print("false")
