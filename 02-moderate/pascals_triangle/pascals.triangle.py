# Reuben Thorpe (2016), CodeEval [Pascals Triangle v1.0]
from sys import argv


def parse_problem(file_path):
    """
        Parse code eval problem set for Pascals Triangle.
    """
    with open(file_path, 'r') as in_file:
        return([int(num) for num in in_file])


def generate_pascals_triangle(depth):
    """
        Generate a pascal triangle of specified depth.
    """
    pascals_triangle = []

    for n in range(depth):
        line = [1]
        for k in range(n):
            line.append(line[k] * (n-k) // (k+1))
        pascals_triangle.append(" ".join(str(num) for num in line))

    return(pascals_triangle)


if __name__ == '__main__':
    problem_sets = parse_problem(argv[1])
    master_triangle = generate_pascals_triangle(max(problem_sets))

    for num in problem_sets:
        print(" ".join(line for line in master_triangle[:num]))
