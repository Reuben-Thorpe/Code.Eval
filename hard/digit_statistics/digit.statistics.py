# Reuben Thorpe (2016), CodeEval [Digit Statistics v1.0]
from sys import argv


def digit_stats(a, n):
    seq_pattern = repeat_seq(a)
    cycle_span = sum(seq_pattern)
    cycle_multiplier = int(n / cycle_span)
    cycle_m_remainder = int(n % cycle_span)

    # Step 1 : Multiply unique remainder sequence by the number of cycles
    seq_pattern = [cycle_multiplier*num for num in seq_pattern]

    # Step 2 : Multiple unique remainder sequence by the cycle remainder
    if cycle_m_remainder != 0:
        m = a
        for i in range(cycle_m_remainder):
            seq_pattern[m] += 1
            m *= a
            m %= 10

    # Print solutions
    for i, num in enumerate(seq_pattern[:-1]):
        print(str(i) + ": " + str(num) + ", ", end="")
    print("9: " + str(seq_pattern[-1]))


def repeat_seq(a):
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
        digit_stats(a, n)
