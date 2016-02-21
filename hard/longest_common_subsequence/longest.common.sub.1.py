# Reuben Thorpe (2016), CodeEval [Longest Common Subseqence v1.0]
from sys import argv
from itertools import product

seeds = []
i = 0


def search(a, b):
    seeds = [char for char in a if char in b]
    while True:
        if all(seed == seeds[0] for seed in seeds):
            break

        seeds = [seed for seed in ("".join(search) for
                 search in product(seeds, (i for i in a))) if
                 check(a, seed) and check(b, seed)]

    return(seeds[0])


def check(string, seed):
    # check seed in a and b
    i = 0
    for char in seed:
        if string.find(char, i) == -1:
            return(False)
        else:
            i = string.find(char, i)+1
    return(True)


def run(filePath):
    data = (line.strip().split(";") for line in open(filePath, 'r') if
            ";" in line)
    for a, b in data:
        if len(a) > len(b):
            print(search(b, a))
        else: 
            print(search(a, b))
        seeds = []

run(argv[1])
