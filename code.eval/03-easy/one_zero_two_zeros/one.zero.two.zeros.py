# Reuben Thorpe (2016), CodeEval [One Zero Two Zeros v1.0]
from sys import argv


def one_zero_two_zero(n, limit):
    """
        Find the number of reverse popcount values of a series which are the
        same as a given value.
    """
    return(sum(dec_to_bin_str(i+1).count('0') == n for i in range(limit)))


def dec_to_bin_str(decimal):
    """
        Convert a decimal to a string representation of its binary form.
        (without leading zeros)
    """
    return '{0:b}'.format(decimal)


if __name__ == '__main__':
    with open(argv[1], 'r') as in_file:
        for line in in_file:
            n, limit = map(int, line.strip().split())
            print(one_zero_two_zero(n, limit))











