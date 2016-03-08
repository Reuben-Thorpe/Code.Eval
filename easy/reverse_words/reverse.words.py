# Reuben Thorpe (2016), CodeEval [Reverse Words v1.1]
from sys import argv


def reverseSentence(line):
    # Reverses words order in a sentence
    line = line.split()
    return(" ".join(word for word in line[::-1]))


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        print(reverseSentence(line))
