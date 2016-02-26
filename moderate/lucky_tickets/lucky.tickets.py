from fractions import Fraction
from sys import argv


def step1(x, y):
    result = 1
    for i in range(y):
        result *= Fraction(x-i, i+1)
    return(result)


def step2(n, i):
    return((-1)**i * step1(n, i) * step1(11*n//2-1-10*i, n-1))


with open(argv[1], "r") as inFile:
    for line in inFile:
        n = int(line)
        print(sum(step2(n, i) for i in range(n//2)))
