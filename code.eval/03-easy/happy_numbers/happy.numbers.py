# Reuben Thorpe (2016), CodeEval [Happy Numbers v1.0]
from sys import argv


def parse_problem(file_path):
    """
        Parse CodeEval problem sets from Happy Numbers.
    """
    with open(file_path, 'r') as in_file:
        for line in in_file:
            yield(sum(int(i)**2 for i in (line.strip())))


def get_digits(n):
    s = 0
    while n:
        yield(n % 10)
        n //= 10


if __name__ == '__main__':
    """
        Code golf solution, decide if a number is 'Happy'.
    """
    unhappy_seq = {4, 16, 37, 58, 89, 145, 42, 20}

    for sqr_sum in parse_problem(argv[1]):

        while True:
            if sqr_sum == 1:
                print('1')
                break

            elif sqr_sum in unhappy_seq:
                print('0')
                break

            else:
                sqr_sum = sum(i**2 for i in get_digits(sqr_sum))
