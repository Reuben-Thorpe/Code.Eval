# Reuben Thorpe (2016), CodeEval [Detecting Cycles v1.0]
from sys import argv


def parse_problem(file_path):
    """
        Parse CodeEval problem sets from 'Detecting Cycles'.
    """
    with open(file_path, 'r') as in_file:
        for line in in_file:
            yield(line.strip().split())


def detect_cycle(seq):
    """
        Detect a cycle of minimum size from within a sequence, the maximum size
        of the sequence for this algorithm is 51 elements.
    """
    cycle = [0]*51

    for index, char in enumerate(seq):
        for i in find_occurences(seq[:index], char):
            if is_repeat_sequence(seq[i:index], seq[index:]):
                if len(seq[i:index]) < len(cycle):
                    cycle = seq[i:index]

    return(cycle)


def find_occurences(seq, char):
    """
        Generate all the indice positions of char in a string.
    """
    for i, element in enumerate(seq):
        if element == char:
            yield(i)


def is_repeat_sequence(r_seq, seq):
    """
        Determin if seq is merly a chained sequence of r_seq.
    """
    l_rseq = len(r_seq)
    l_seq = len(seq)

    if not (l_seq % l_rseq):
        for i in range(l_rseq, l_seq, l_rseq):
            if seq[i-l_rseq:i] != r_seq:
                return(False)

        return(True)

    else:
        return(False)


if __name__ == '__main__':
    for seq in parse_problem(argv[1]):
        print(' '.join(detect_cycle(seq)))
