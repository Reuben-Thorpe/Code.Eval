# Reuben Thorpe (2016), CodeEval [Game Of Life v1.0]
from sys import argv


def switch(r, c, grid, N):
    # Determin if game of life pixle should be flipped
    state = grid[r][c]
    nearest_on = sum(['*' in grid[row][column] for
                     row in [r-1, r, r+1] for
                     column in [c-1, c, c+1] if
                     [row, column] != [r, c] and column >= 0 and
                     column <= N-1 and row >= 0 and row <= N-1])

    if '*' == state:
        if nearest_on == 2 or nearest_on == 3:
            return('*')
        else:
            return('.')
    else:
        if nearest_on == 3:
            return('*')
        else:
            return('.')


def get_last_frame_cgl(N, steps, grid):
    # Recursive algorithm to produce final frame of conways game of life
    if steps == 0:
        return grid

    else:
        new_grid = [[switch(x, y, grid, N) for
                     y in range(N)] for x in range(N)]

        if new_grid == grid:
            return grid
        else:
            return(get_last_frame_cgl(N, steps-1, new_grid))


if __name__ == "__main__":
    initial_frame = [[pixle for pixle in line.strip()] for
                     line in open(argv[1], "r")]

    N = len(initial_frame[0])
    last_frame = get_last_frame_cgl(N, 10, initial_frame)

    for row in last_frame:
        print("".join(row))
