# Reuben Thorpe (2016) Longest Lines

from sys import argv

if __name__ == "__main__":
    with open(argv[1], "r") as inFile:
        n = int(inFile.readline())
        lst = sorted((line[:-1] for line in inFile), key=len, reverse=True)
        for i in range(n):
            print(lst[i])
