# Reuben Thorpe (2016), CodeEval [Longest Common Subseqence v1.1]
from sys import argv
from itertools import product


def search(a, b):
    seeds = {char for char in a if char in b}
    while True:
        if len(seeds) == 1:
            break

        seeds = {seed for seed in ("".join(search) for
                 search in product(seeds, (i for i in a))) if
                 check(a, seed) and check(b, seed)}

    result = [result for result in seeds][0]
    return(result)


def check(string, seed):
    # check seed in a and b
    i = 0
    for char in seed:
        if string.find(char, i) == -1:
            return(False)
        else:
            i = string.find(char, i)+1
    return(True)


def main(filePath):
    data = (line.strip().split(";") for line in open(filePath, 'r') if
            ";" in line)

    for a, b in data:
        if len(a) > len(b):
            print(search(b, a))
        else:
            print(search(a, b))

if __name__ == "__main__":
    main(argv[1])
