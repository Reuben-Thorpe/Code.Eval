# Reuben Thorpe (2015) , 7th December Advent of Code

from numpy import uint16


def run(fileName):
    value = {}
    length = 0
    data = open(fileName)
    data = [line.replace('\n', '').split() for line in data]
    complete = False

    logic = {"RSHIFT": ">>",
             "LSHIFT": "<<",
             "AND": "&"}

    while not complete:
        complete = True

        for line in data:

            if line[1] in ["RSHIFT", "LSHIFT", "AND"]:
                if line[0] in value and (line[2].isdigit()):

                    exec("value[line[4]] = value[line[0]] " +
                         logic[line[1]] + " uint16(line[2])")

                elif line[0].isdigit() and line[2] in value:

                    exec("value[line[4]] = uint16(line[0]) " +
                         logic[line[1]] + "value[line[2]]")

                elif line[0] in value and line[2] in value:

                    exec("value[line[4]] = value[line[0]] " +
                         logic[line[1]] + " value[line[2]]")

                else:
                    complete = False
                    continue

            elif line[1] == "->":
                if line[0].isdigit():
                    value[line[2]] = uint16(line[0])
                elif line[0] in value:
                    value[line[2]] = value[line[0]]
                else:
                    complete = False
                    continue

            elif line[1] == "OR":
                if line[0] in value and line[2] in value:
                    value[line[4]] = value[line[0]] | value[line[2]]
                elif line[0] in value and line[2].isdigit():
                    value[line[4]] = value[line[0]] | uint16(line[2])
                elif line[0].isdigit() and line[2] in value:
                    value[line[4]] = uint16(line[0]) | value[line[2]]
                else:
                    complete = False
                    continue

            elif line[0] == "NOT":
                if line[1] in value:
                    value[line[3]] = ~ value[line[1]]
                elif line[1].isdigit():
                    value[line[3]] = ~ uint16(line[1])
                else:
                    complete = False
                    continue

        if length == len(value):
            print("PROGRAM HAS ENTERED A INFINIT LOOP --- HALTING!!")
            print("\nDEBUG")
            print(value)
            exit()
        length = len(value)

    print("The Solution to '", fileName, "' = ", value['a'])

run("input.1.txt")
run("input.2.txt")
