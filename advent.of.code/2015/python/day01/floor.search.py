# Reuben Thorpe (2015) , 1st December Advent of code


def findFloor():
    data = open('input.txt', 'r').read()
    floor = 0
    flag = False
    for index, i in enumerate(data, start=1):
        if (i == "("):
            floor += 1
        elif (i == ")"):
            floor -= 1

        if (not flag and floor == -1):
            basmentIndex = index
            flag = True

    print("\nPart 1 = ", floor)
    print("Part 2 = ", basmentIndex, "\n")


findFloor()
