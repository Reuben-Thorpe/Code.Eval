# Reuben Thorpe (2016), CodeEval [Data Recovery v1.0]
from itertools import count
from sys import argv


def recover(text, decoder):
    """
    Swap words in the text specified by a puzzle in the decoder sequence.
    """
    decoded = [x for y, x in sorted(zip(decoder, text))]

    for missing_index in count():
        if missing_index not in decoder:
            decoded.insert(missing_index, text[-1])
            break

    decoded = " ".join(decoded)
    return(decoded)


if __name__ == "__main__":
    with open(argv[1], "r") as in_file:
        for line in in_file:
            text, decoder = line.split(";")
            decoder = [(int(i) - 1) for i in decoder.split()]
            text = text.split()
            print(recover(text, decoder))

