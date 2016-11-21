from sys import argv


def parse_problem(file_path):
    """
        Parse CodeEval each set a time for Sudoku.
    """
    with open(file_path, 'r') as in_file:
        for line in in_file:
            grid, seq =line.split(';')
            grid = int(grid)
            seq = seq.strip().split(',')

            matrix = [seq[i-grid:i] for i in range(grid, (grid*grid) + 1, grid)]
            yield(matrix)


def gfq_sets(matrix, N, size):
    """
        Generate all possible square quadrants of a matrices. Also flattern
        these matrices and only include unique entries.

        Abbriviation = generate flat quadrant sets.
    """
    for y in range(size, N + 1, size):
        y_slice = matrix[y-size:y]
        for x in range(size, N + 1, size):
            yield({i for row in y_slice for i in row[x-size:x]})


def sudoku(matrix):
    """
        Check whether a matrix is a valid sudoku entry.
    """
    N = len(matrix)
    quadrant_size = 3 if N == 9 else 2

    # Check rows
    if any(len(set(row)) < N for row in matrix):
        return(False)

    # Check colums
    elif any(len({matrix[x][y] for y in range(N)}) < N for x in range(N)):
        return(False)

    # Check quadrants
    elif any(len(quad) < N for quad in gfq_sets(matrix, N, quadrant_size)):
        return(False)

    else:
        return(True)


if __name__ == '__main__':
    for problem in parse_problem(argv[1]):
        print(sudoku(problem))







