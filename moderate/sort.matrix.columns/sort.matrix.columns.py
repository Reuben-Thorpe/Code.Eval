# Reuben Thorpe (2016), CodeEval [Sort Matrix Columns v1.0]
from sys import argv
from copy import deepcopy


def sortedColumns(matrix):
    """
    Sorts the columns in the matrix by the first row in ascending order.
    If the numbers in the first line are equal, sort it by the lowest number
    of following line. This function does not consume the input matrix
    """
    M1 = deepcopy(matrix)
    NN = len(M1[0])
    MM = len(M1)
    colSlice = [[0, (NN-1)]]

    for row in range(MM):
        for col1, col2 in colSlice:
            sortByRowSlice(M1, MM, row, col1, col2)

        colSlice = [[i, i + M1[row].count(num)-1] for
                    i, num in enumerate(M1[row]) if
                    M1[row].index(num) == i and
                    M1[row].count(num) > 1]

        if colSlice == []:
            break

    return(M1)


def sortByRowSlice(matrix, MM, row, col1, col2):
    """
    Sorts matrix rows after "row" based on a sort of the slice "row[col1:col2]"
    """
    sortRow = [[matrix[row][i], i] for i in range(col1, col2+1)]
    sortRow = [i for num, i in sorted(sortRow)]

    for section in range(row, MM):
        matrix[section][col1:col2+1] = [matrix[section][i] for i in sortRow]


def printOutput(matrix):
    """
    Prints matrix in the standard output for "sort matrix columns" challange
    """
    MM = len(matrix)-1

    for i, row in enumerate(matrix):
        if i != MM:
            for num in row:
                print(num, end=" ")
            print(end="| ")
        else:
            NN = len(matrix[0])-1
            for j, num in enumerate(row):
                if j != NN:
                    print(num, end=" ")
                else:
                    print(num)


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        matrix = [[int(col) for col in row.split()] for row in line.split('|')]
        matrix = sortedColumns(matrix)
        printOutput(matrix)
