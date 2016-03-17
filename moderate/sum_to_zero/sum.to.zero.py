# Reuben Thorpe (2016), CodeEval [Sum To Zero v1.0]
from itertools import combinations
from sys import argv

def sum_to_zero(sequence):
    """
        Counts the numbers of ways in which the sum of 4 elements in the
        sequence results in zero.
    """
    return(sum(1 for comb in combinations(sequence, 4) if sum(comb) == 0))


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        line = tuple(int(num) for num in line.split(','))
        print(sum_to_zero(line))
