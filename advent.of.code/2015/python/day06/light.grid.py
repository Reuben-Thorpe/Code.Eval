# Reuben Thorpe (2015) , 5th December Advent of Code

grid_1 = [[0] * 1000 for i in range(1000)]
grid_2 = [[0] * 1000 for i in range(1000)]

data = [line.split() for line in
        open('input.txt', 'r').read().split('\n')][:-1]


def switch(first, last, mode):
    # Part 1
    first = [int(i) for i in first.split(",")]
    last = [int(i) for i in last.split(",")]
    if mode is 't':
        for x in range(first[0], (last[0]+1)):
            for y in range(first[1], (last[1]+1)):
                if (grid_1[x][y] == 1):
                    grid_1[x][y] = 0
                else:
                    grid_1[x][y] = 1

    else:
        for x in range(first[0], (last[0]+1)):
            for y in range(first[1], (last[1]+1)):
                grid_1[x][y] = mode


def dimmer(first, last, mode):
    # Part 2
    first = [int(i) for i in first.split(",")]
    last = [int(i) for i in last.split(",")]
    if mode is 't':
        for x in range(first[0], (last[0]+1)):
            for y in range(first[1], (last[1]+1)):
                grid_2[x][y] += 2

    else:
        for x in range(first[0], (last[0]+1)):
            for y in range(first[1], (last[1]+1)):
                if mode == 1:
                    grid_2[x][y] += 1
                elif grid_2[x][y] != 0:
                    grid_2[x][y] -= 1

for line in data:
    if line[0] == 'turn':
        if line[1] == 'on':
            switch(line[2], line[4], 1)
            dimmer(line[2], line[4], 1)
        else:
            switch(line[2], line[4], 0)
            dimmer(line[2], line[4], 0)
    else:
        switch(line[1], line[3], 't')
        dimmer(line[1], line[3], 't')

part_1 = sum(i.count(1) for i in grid_1)
part_2 = sum(sum(i) for i in grid_2)

print("\nPart 1 =", part_1)
print("Part 2 =", part_2, "\n")
