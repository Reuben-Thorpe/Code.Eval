# Reuben Thorpe (2015) 11th December Advent of Code [TSP]
from itertools import permutations
from math import factorial
import re

PARSE = r"(\S+) would (\S+) (\d+) happiness units by sitting next to (\S+)\."


def search(fileName):
    data = re.compile(PARSE).findall(open(fileName, 'r').read())
    names = list({line[i] for line in data for i in [0, 3]})
    n = len(names)
    limit = factorial(n)/2
    tables_1 = []
    tables_2 = []

    for i, perm in enumerate(permutations(names)):
        if i > limit:
            break

        table = [int(pair[2]) if pair[1] == 'gain' else -
                 int(pair[2]) for
                 i in range(n-1) for
                 pair in data if
                 perm[i] in [pair[0], pair[3]] and
                 perm[i+1] in [pair[0], pair[3]]]

        tables_2 += [sum(table)]

        table += [int(pair[2]) if pair[1] == 'gain' else -
                  int(pair[2]) for
                  pair in data if
                  perm[n-1] in [pair[0], pair[3]] and
                  perm[0] in [pair[0], pair[3]]]

        tables_1 += [sum(table)]

    print("\nPart 1 = ", max(tables_1))
    print("Part 2 = ", max(tables_2), "\n")


if __name__ == '__main__':
    search('input.txt')
