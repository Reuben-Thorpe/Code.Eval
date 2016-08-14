# Reuben Thorpe (2016), CodeEval [Pangrams v1.0]
from sys import argv
from string import ascii_lowercase


def parse_problem(file_path):
    with open(argv[1], 'r') as in_file:
        for line in in_file:
            yield(set(char for char in line.strip().lower().replace(' ','')))





if __name__ == '__main__':
    alphabet = set(ascii_lowercase)

    for problem in parse_problem(argv[1]):
        solution = ''.join(sorted(char for char in
                                  alphabet.difference(problem)))

        print(solution) if solution else print('NULL')
