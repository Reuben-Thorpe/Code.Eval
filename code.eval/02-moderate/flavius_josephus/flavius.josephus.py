# Reuben Thorpe (2016), CodeEval [Flavius Josephus v1.0]
from sys import argv


def flavius_josephus_recusivus(seq, N, M):
    """
        My recursive solution to the flavius josephus scenario.

        seq = A list of participants which are alive.
         N  = The number of people currently alive.
         M  = Mth person who is destined to die.
    """
    if N > M:
        R = N % M
        output = seq[M-1::M]
        del seq[M-1::M]
        N = N - (N // M)
        seq = seq[-R:] + seq[:-R]
        return(output + flavius_josephus_recusivus(seq, N, M))

    elif N == M:
        return(seq[-1:] + flavius_josephus_recusivus(seq[:-1], N-1, M))

    elif N > 1:
        offset_index = (M % N) - 1
        output = [seq[offset_index]]
        del seq[offset_index]

        if offset_index > 0:
            seq = seq[offset_index:] + seq[:offset_index]
        else:
            seq = seq[:offset_index] + seq[offset_index:]

        return(output + flavius_josephus_recusivus(seq, N-1, M))

    else:
        return(seq)


if __name__ == "__main__":
    with open(argv[1], 'r') as in_file:
        for line in in_file:
            N, M = [int(num) for num in line.split(',')]
            seq = [num for num in range(N)]
            print(" ".join(map(str, flavius_josephus_recusivus(seq, N, M))))

