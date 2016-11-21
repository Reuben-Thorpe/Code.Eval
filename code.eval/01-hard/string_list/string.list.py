# Reuben Thorpe (2016), CodeEval [String List v1.1]
from sys import argv
from itertools import product


def parse_problem(file_path):
    """
        Parse CodeEval problem sets for String List.
    """
    with open(file_path, 'r') as in_file:
        for line in in_file:
            N, seq = line.strip().replace(' ', '').split(',')
            yield(int(N), sorted(set(seq)))



if __name__ == '__main__':
    """
        Code golf solution!
    """
    for problem in parse_problem(argv[1]):
        N, seq = problem
        print(','.join(''.join(comb) for comb in product(seq, repeat=N)))
