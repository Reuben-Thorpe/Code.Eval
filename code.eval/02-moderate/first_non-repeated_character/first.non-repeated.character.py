# Reuben Thorpe (2016), CodeEval [First Non-Repeated Character v1.0]
from sys import argv


with open(argv[1], "r") as in_file:
    for line in in_file:
        for char in line:
            if line.count(char) == 1:
                print(char)
                break
