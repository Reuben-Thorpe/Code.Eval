# Reuben Thorpe (2015), CodeEval [Bubble Sort v1.0]
from sys import argv


def bubbleSort(data, iteration):
    """
    Completes n iterations of the bubble sort algorithm on 'data'.
    Then if prints the output in the standard format
    """

    for i in range(iteration):
        # Single iteration of bubble sort
        done = True
        for i in lenD:
            if data[i+1] < data[i]:
                data[i], data[i+1] = data[i+1], data[i]
                done = False
        if done is True:
            break

    # Prints with standard formating
    for i in lenD:
        print(str(data[i])+" ", end="")
    print(data[-1])


if __name__ == "__main__":

    parse = ([[int(i) for i in data.split()], int(iteration)] for
             data, iteration in (line.split("|") for
                                 line in open(argv[1], 'r')))

    for data, iteration in parse:
        lenD = range(len(data) - 1)
        if lenD != 0:
            bubbleSort(data, iteration)
        else:
            print(data[0])
