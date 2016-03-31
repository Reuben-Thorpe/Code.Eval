# Reuben Thorpe (2016), CodeEval [Minimum Coins v1.0]
from sys import argv


def min_coins(num):
    num_coins = num // 5
    num %= 5
    num_coins += num // 3
    num %= 3
    num_coins += num
    return(num_coins)


if __name__ == "__main__":
    for num in open(argv[1], "r"):
        print(min_coins(int(num)))
