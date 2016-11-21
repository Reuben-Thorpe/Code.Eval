# Reuben Thorpe (2015), CodeEval [Fibonacci Series v1.1]
from math import sqrt
from sys import argv


PHI = 1.61803398874989484820
SQRT_5 = sqrt(5)


def fib(n):
    return(round(((PHI**n)-(-PHI)**(-n))/SQRT_5))


if __name__ == "__main__":
    for num in open(argv[1], 'r'):
        print(fib(int(num)))
