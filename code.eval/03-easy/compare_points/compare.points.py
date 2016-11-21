# Reuben Thorpe (2016), CodeEval [Compare Points v1.0]
from collections import namedtuple
from sys import argv


def parse_problem(file_path):
    """
        Parse the CodeEval problem 'Compare Points'.
    """
    Gps = namedtuple('Gps', ['o', 'p', 'q', 'r'])

    with open(file_path, 'r') as in_file:
        for line in in_file:
            nums = [int(num) for num in line.strip().split()]
            yield(Gps(*nums))


def get_heading(gps):
    """
        Generate the heading from one gps coordinate to the second. The second
        coordinate is transformed with the first so that its origin become
        (0,0). The cardinal direction is then simple to extrapolate.
    """
    x = gps.q - gps.o
    y = gps.r - gps.p

    cardinal_string = ""

    if y > 0:
        cardinal_string += 'N'
    elif y < 0:
        cardinal_string += 'S'

    if x > 0:
        cardinal_string += 'E'
    elif x < 0:
        cardinal_string += 'W'

    return(cardinal_string if cardinal_string else 'here')


if __name__ == '__main__':
    for gps in parse_problem(argv[1]):
        print(get_heading(gps))
