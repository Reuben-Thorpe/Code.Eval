# Reuben Thorpe (2015) , 2nd December Advent of Code


def wrapper():
    wrapperTotal = 0
    ribbionTotal = 0
    data = open("input.txt")
    for line in data:
        line = line.strip().split("x")
        line = sorted(int(i) for i in line)

        wrapperTotal += (2*(line[0]*line[1]) +
                         2*(line[1]*line[2]) +
                         2*(line[2]*line[0]) +
                         line[0]*line[1])

        ribbionTotal += (sum(2*line[i] for i in range(2)) +
                         line[0]*line[1]*line[2])

    print("\nPart 1 =", wrapperTotal)
    print("Part 2 =", ribbionTotal, "\n")


wrapper()
