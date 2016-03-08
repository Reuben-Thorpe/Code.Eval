# Reuben Thorpe (2016), CodeEval [Palindromic Ranges v1.0]
from sys import argv
from itertools import product


def getAllSubRanges(string):
    """
    Generator which produces all possible subsequences of a string
    """
    length = range(len(string))
    for i, j in product(length, length):
        yield string[i:j+1]


def palindromicRanges(L, R):
    """
    Generate all the palindromic ranges between L, R
    """
    pRange = []

    for i in range(L, R+1):
        i = str(i)
        lenNum = len(i)
        r = int(lenNum/2)

        if lenNum % 2 == 0:
            pRange.append(int(i[0:r] == i[r:lenNum+1][::-1]))

        else:
            if lenNum == 1:
                pRange.append(1)
            else:
                pRange.append(int(i[0:r] == i[r+1:3][::-1]))

    result = sum(1 for sub in getAllSubRanges(pRange) if
                 sub.count(1) % 2 == 0 and sub != [])

    return(result)


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        L, R = (int(num) for num in line.strip().split())
        print(palindromicRanges(L, R))
