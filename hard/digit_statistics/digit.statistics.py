# Reuben Thorpe (2016), CodeEval [Digit Statistics v1.0]
from sys import argv


def stats(a, n):
    values = pattern(a)
    lenR = sum(values)
    repeat = n/lenR
    cycle = int(repeat)
    cycleR = int((repeat % 1)*lenR)

    # Step 1 : Multiply unique remainder sequence by the number of cycles
    values = [cycle*value for value in values]

    # Step 2 : Multiple unique remainder sequence by the cycle remainder
    if cycleR != 0:
        m = a
        for i in range(cycleR):
            values[m] += 1
            m *= a
            m %= 10

    # Print solutions
    for i, value in enumerate(values[:-1]):
        print(str(i) + ": " + str(value) + ", ", end="")
    print("9: " + str(values[-1]))


def pattern(a):
    # Finds unique repeat in last digits of a^i sequence
    m = a
    seq = [0]*10
    while seq[m] == 0:
        seq[m] += 1
        m *= a
        m %= 10
    return(seq)


if __name__ == "__main__":
    pairs = ([int(num) for num in line.split()] for line in open(argv[1], 'r'))

    for a, n in pairs:
        stats(a, n)
