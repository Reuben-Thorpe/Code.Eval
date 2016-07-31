# Reuben Thorpe (2016), CodeEval [Code Combinations v1.0]
from sys import argv
from itertools import product


def parse_problem(file_path):
    """
        Parse individual CodeEval problem sets from the challange
        code combination.
    """
    with open(file_path, "r") as in_file:
        for line in in_file:
            problem = line.replace(" ","").strip().split("|")
            yield(problem)


def generate_submatrices(matrix, size):
    """
        Generate all square sub matrices of size "S" from its parent matrix.
    """
    S = size
    N = len(matrix[0]) + 1
    M = len(matrix) + 1

    for i, j in product(range(S, M), range(S, N)):
       yield(set(char for row in matrix[i-S:i] for char in row[j-S:j]))



if __name__ == "__main__":
    match_string = "code"

    for problem in parse_problem(argv[1]):
        counter = 0
        for twobytwo in generate_submatrices(problem, 2):
            if all(char in twobytwo for char in match_string):
                counter += 1
        print(counter)
