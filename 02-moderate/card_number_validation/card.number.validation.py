# Reuben Thorpe (2016), CodeEval [Card Number Validation v1.0]
from sys import argv


def luhn(n):
    """luhnsum(int)->bool
    Mod 10 checksum by Hans Peter Luhn (1896-1964)
    """
    l_sum=0
    while n:
        r=n%100
        n//=100
        z=r%10
        r=r//10*2
        l_sum+=r//10+r%10+z
    return(1 if 0==l_sum%10 else 0)


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        card_number = int(line.replace(" ",""))
        print(luhn(card_number))
