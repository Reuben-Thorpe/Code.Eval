# Reuben Thorpe (2015) , 8th December Advent of Code 2015


def part1(fileName):
    stringLiteral = 0
    stringRep = 0
    data = open(fileName)

    for i in data:
        stringLiteral += len(i.replace("\n", ""))
        stringRep += len(eval(i))

    print("Part 1 = ", (stringLiteral-stringRep))


def part2(fileName):
    stringLiteral = 0
    stringRep = 0
    data = open(fileName)
    for i in data:
        i = i.replace("\n", "")
        i = i.replace("\\", "\\\\")
        i = i.replace("\"", "\\\"")
        i = '"' + i + '"'
        stringLiteral += len(i)
        stringRep += len(eval(i))
    print("Part 2 = ", (stringLiteral-stringRep))


if __name__ == '__main__':
    part1('input.txt')
    part2('input.txt')
