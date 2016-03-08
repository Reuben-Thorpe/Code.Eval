# Reuben Thorpe (2016), CodeEval [Longest Common Subseqence v1.1]
from sys import argv
from itertools import product


def getLongestCommonSub(a, b):
    """
    Generates all possible groupings that could be in a & b
    and then returns the longest of these subsequences.
    """
    seeds = {char for char in a if char in b}
    while True:
        if len(seeds) == 1:
            break

        seeds = {seed for seed in ("".join(search) for
                 search in product(seeds, (i for i in a))) if
                 check(a, seed) and check(b, seed)}

    result = [result for result in seeds][0]
    return(result)


def check(string, sub):
    """
    Check if subSeq is in string, characters can be removed from string.
    """
    i = 0
    for char in sub:
        if string.find(char, i) == -1:
            return(False)
        else:
            i = string.find(char, i)+1
    return(True)



if __name__ == "__main__":
    data = (line.strip().split(";") for line in open(argv[1], 'r') if
            ";" in line)

    for a, b in data:
        if len(a) > len(b):
            print(getLongestCommonSub(b, a))
        else:
            print(getLongestCommonSub(a, b))
