# Reuben Thorpe (2016), CodeEval [Array Absurdity v1.0]
from sys import argv


with open(argv[1], 'r') as in_file:
    for line in in_file:
        N, seq = line.split(';')
        seq = [int(num) for num in seq.split(',')]
        length = int(N) - 1

        for i in range(length):
            if seq[i] in seq[i+1:]:
                print(seq[i])
                break
