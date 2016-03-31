# Reuben Thorpe (2016), CodeEval [Repeated Sub String v1.0]
from sys import argv


def findSubString(line):
    """
    Finds the first found, max length, non-overlapping repeated sub-sequence
    in a string. returns "NONE" if none found.
    """
    line = line.strip()
    subLen = lineLen = len(line)

    while subLen > 0:
        for i in range((lineLen-subLen)+1):
            subSeq = line[i:i+subLen]
            if subSeq in line[0:i] or subSeq in line[i+subLen:lineLen]:
                if subSeq != " ":
                    return(subSeq)
        subLen -= 1
    return("NONE")


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        print(findSubString(line))
