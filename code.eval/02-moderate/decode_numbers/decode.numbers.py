# Reuben Thorpe (2016), CodeEval [Decode Numbers v1.0]
from sys import argv


def decode_permutations(number_string):
    """ Dynamic programming solution to the possible decoding problem """

    int_array = [int(i) for i in number_string]
    n = len(int_array) + 1
    count = [0] * n
    count[0] = 1
    count[1] = 1

    for i in range(2, n):

        if int_array[i-1] > 0:
            count[i] = count[i-1]

        if int_array[i-2] < 2 or (int_array[i-2] == 2 and int_array[i-1] < 7):
            count[i] += count[i-2]

    return(count[-1])


if __name__ == "__main__":
    with open(argv[1], "r") as in_file:
        for line in in_file:
            number_string = line.strip()
            print(decode_permutations(number_string))
