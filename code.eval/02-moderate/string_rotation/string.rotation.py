# Reuben Thorpe (2016), CodeEval [String Rotation v1.0]
from sys import argv


with open(argv[1], 'r') as in_file:
    for line in in_file:
        string, rotation = line.strip().split(',')

        if rotation.count(string[0]) == 1:
            splice = rotation.index(string[0])
            print(string == rotation[splice:] + rotation[:splice])

        else:
            indicies_of_char = {i for i, char in enumerate(rotation) if
                                char == string[0]}


            print(any(string == rotation[splice:] + rotation[:splice] for
                      splice in indicies_of_char))
