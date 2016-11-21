# Reuben Thorpe (2016), CodeEval [Clean Up Words v1.0]
from sys import argv


for line in open(argv[1], "r"):
    new_line = "".join(char if char.isalpha() == True else " " for char in line)
    new_line = new_line.split()
    new_line = " ".join(new_line).lower()
    print(new_line)


