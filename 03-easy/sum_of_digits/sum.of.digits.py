# Reuben Thorpe (2016), CodeEval [Sum of Digits v1.0]
from sys import argv

with open(argv[1], "r") as in_file:
    for line in in_file:
        print(sum(int(num) for num in line.strip()))
