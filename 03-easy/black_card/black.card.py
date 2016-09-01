# Reuben Thorpe (2016), CodeEval [Black Card v1.1]
from sys import argv


def parse_problem(file_path):
    # Parse problem from the CodeEval problem "Black Card".
    with open(file_path, "r") as in_file:
        for line in in_file:
            names, turns = line.strip().split("|")
            turns = int(turns)
            names = names.split()
            yield(names, turns)


def black_card(names, turns):
    # Determin which card in a sequence of names is the "black card".
    name_count = len(names)

    while (name_count > 1):
        del names[(turns % name_count) - 1]
        name_count = len(names)

    return(names[0])


if __name__ == "__main__":
    for names, turns in parse_problem(argv[1]):
        print(black_card(names, turns))
