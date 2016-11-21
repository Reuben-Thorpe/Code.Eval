# Reuben Thorpe (2016), CodeEval [Time To Eat v1.1]
from sys import argv


def main(fileName):
    # Parse and sort time stamp strings
    for line in open(fileName, "r"):
        for result in sorted(line.split(), reverse=True):
            print(result+" ", end="")
        print()


if __name__ == "__main__":
    main(argv[1])
