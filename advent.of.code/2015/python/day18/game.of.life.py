# Reuben Thorpe (2015) , Advent of Code 18th December [Conway Game of life]


STEPS = 100	# Number of animation frames
DIM = 100	# Side dimension of array


def switch(r, c, state, grid):
    if state == 'p#':
        return('p#')
    else:
        nearestOn = sum(['#' in grid[row][column] for
                        row in [r-1, r, r+1] for
                        column in [c-1, c, c+1] if
                        [row, column] != [r, c] and column >= 0 and
                        column <= DIM-1 and row >= 0 and row <= DIM-1])
        if '#' == state:
            if nearestOn == 2 or nearestOn == 3:
                return('#')
            else:
                return('.')
        else:
            if nearestOn == 3:
                return('#')
            else:
                return('.')


def step(n, grid):
    # Recursive algorithm to produce frames for conways game of life
    if n == 0:
        return grid
    else:
        newGrid = [['.'] * DIM for i in range(DIM)]
        for r, line in enumerate(grid):
            for c, state in enumerate(line):
                newGrid[r][c] = switch(r, c, state, grid)

        return(step(n-1, newGrid))


def part1(fileName):
    grid = [[light for light in line.strip()] for line in open(fileName)]
    result = step(STEPS, grid)
    answer = sum(row.count('#') + row.count('p#') for row in result)
    print("\nPart 1 = ", answer)


def part2(fileName):
    grid = [[light for light in line.strip()] for line in open(fileName)]
    grid[0][0] = 'p#'
    grid[0][DIM-1] = 'p#'
    grid[DIM-1][0] = 'p#'
    grid[DIM-1][DIM-1] = 'p#'
    result = step(STEPS, grid)
    answer = sum(row.count('#') + row.count('p#') for row in result)
    print("Part 2 = ", answer, "\n")


part1('input.txt')
part2('input.txt')
