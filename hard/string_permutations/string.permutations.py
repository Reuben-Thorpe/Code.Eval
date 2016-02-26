# Reuben Thorpe (2016), CodeEval [String Permutations v1.0]

from sys import argv
from itertools import permutations as perm
from math import factorial


def sort(fileName):

    for line in open(fileName, 'r'):
        n = len(line.strip())
        limit = factorial(n)
        digits = sorted((char for char in line if char.isdigit()))
        alphaUpper = sorted((char for char in line if char.isupper()))
        alphaLower = sorted((char for char in line if char.islower()))

        for i, seq in enumerate(perm(digits + alphaUpper + alphaLower)):
            print("".join(seq), end="")
            if i < limit-1:
                print(",", end="")
            else:
                print()


if __name__ == "__main__":
    sort(argv[1])
