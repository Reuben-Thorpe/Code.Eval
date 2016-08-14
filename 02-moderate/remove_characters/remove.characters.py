# Reuben Thorpe (2016), CodeEval [Remove Characters v1.1]
from sys import argv


def parse_problem(file_path):
    with open(argv[1], 'r') as in_file:
        for line in in_file:
            yield(line.strip().split(", "))


if __name__ == '__main__':
    for problem in parse_problem(argv[1]):
        sentence, remove_char = problem

        for char in remove_char:
            sentence = sentence.replace(char, '')

        print(sentence)
