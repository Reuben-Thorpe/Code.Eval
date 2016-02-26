# Reuben Thorpe (2016)
from sys import argv


def stats(a, n):
    values = pattern(a)
    lenR = sum(values)
    repeat = n/lenR
    step1 = int(repeat)
    step2 = int((repeat % 1)*lenR)

    # Step 1 : multiply by general repeat
    values = [step1*value for value in values]

    # Step 2 : add remainders of repeat
    if step2 != 0:
        m = a
        for i in range(step2):
            values[m] += 1
            m *= a
            m %= 10

    # Print solutions
    for i, value in enumerate(values[:-1]):
        print(str(i) + ": " + str(value) + ", ", end="")
    print("9: " + str(values[-1]))


def pattern(a):
    # Finds repeat pattern in last digits of sequence
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
