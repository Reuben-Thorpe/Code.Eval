# Reuben Thorpe (2016), CodeEval [Distinct Subsequence v1.0]
# NOTE : USING SETS MY BE FASTER BUT UNSTABLE, CONVERT TO CLASS
from sys import argv


def findIn(inString, char):
    # Returns all position indicies of char in string
    return([i for i, check in enumerate(inString) if check is char])


def distSub(seq, subSeq):
    """ Generates position matrix, and then counts the number of distinct
         sub-sequences with recursion. The print results
    """
    freqMatrix = []

    for char in subSeq:
        freqMatrix.append(findIn(seq, char))

    countSub(freqMatrix, 0, 0)
    print(gResult)


def countSub(freqMatrix, depth, cut):
    """ Counts the number of sub-sequences in the position matrix.
        This function used global variable "gResult" and "gLimit"
    """
    global gLimit
    if depth is 0:
        for i in freqMatrix[0]:
            countSub(freqMatrix, depth+1, i)

    elif depth is gLimit:
        global gResult
        for i in freqMatrix[depth]:
            if i > cut:
                gResult += 1

    else:
        for i in freqMatrix[depth]:
            if i > cut:
                countSub(freqMatrix, depth+1, i)


if __name__ == "__main__":
    gLimit = gResult = 0
    for line in open(argv[1], "r"):
        seq, subSeq = line.strip().split(',')
        gLimit = len(subSeq)-1
        distSub(seq, subSeq)
        gResult = 0;
