# Reuben Thorpe (2016), CodeEval [Time To Eat v1.0]
from sys import argv


def stampWeight(line):
    # Weights a time stamp string, format "HH:MM:SS"
    return(sum(int(num)*i for num, i in zip(line.split(":"), [10000, 100, 1])))


def main(fileName):
    # Parse and sort time stamp strings
    inFile = open(fileName, "r")
    for line in inFile:
        for result in sorted(line.split(), key=stampWeight, reverse=True):
            print(result+" ", end="")
        print()


if __name__ == "__main__":
    main(argv[1])
