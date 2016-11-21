# Reuben Thorpe (2015) , Advent of Code 18th December [Conway Game of Life]

from time import sleep
import curses

STEPS = 100	# Number of animation frames
DIM = 100	# Width of array
FPS = 30	# Frame per second


def switch(r, c, state, grid):
    # Main switching algorithm
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
        return [grid]

    else:
        newGrid = [['.'] * DIM for i in range(DIM)]
        for r, line in enumerate(grid):
            for c, state in enumerate(line):
                newGrid[r][c] = switch(r, c, state, grid)

        return([grid]+step(n-1, newGrid))


def animate(frames):
    # Animates the result frames (within the command line)
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    try:
        for frame in frames:
            maxLength = int(stdscr.getmaxyx()[0])
            for i, line in enumerate(frame):
                if i < maxLength-1:
                    stdscr.addstr(i, 0, "".join(line).replace("p#", "#"))
                    stdscr.refresh()
                    sleep(1/FPS)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()


def part1(fileName):
    # Solutions to part1
    print("Pre-rendering frames for part 1 ......")
    grid = [[light for light in line.strip()] for line in open(fileName)]
    results = step(STEPS, grid)
    animate(results)
    answer = sum(row.count('#') + row.count('p#') for row in results[STEPS])
    print("\nPart 1 = ", answer, "\n")


def part2(fileName):
    # Solutions to part2
    print("Pre-rendering frames for part 2 ......")
    grid = [[light for light in line.strip()] for line in open(fileName)]
    grid[0][0] = 'p#'
    grid[0][DIM-1] = 'p#'
    grid[DIM-1][0] = 'p#'
    grid[DIM-1][DIM-1] = 'p#'
    results = step(STEPS, grid)
    animate(results)
    answer = sum(row.count('#') + row.count('p#') for row in results[STEPS])
    print("\nPart 2 = ", answer, "\n")


part1('input.txt')
part2('input.txt')
