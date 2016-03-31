# Reuben Thorpe (2016), CodeEval [Distinct Subsequence v1.0]
from sys import argv

def distSub(seq, subSeq):
    """
    Generates position matrix, and then counts the number of distinct
    sub-sequences with recursion. The print results
    """
    result = 0
    limit = len(subSeq)-1

    def findIn(inString, char):
        """
        Returns all position indicies of char in string
        """
        return([i for i, check in enumerate(inString) if check is char])


    def countSub(freqMatrix, depth, cut):
        """
        Counts the number of sub-sequences in the position matrix.
        """
        nonlocal result
        nonlocal limit

        if depth is 0:
            for i in freqMatrix[0]:
                countSub(freqMatrix, depth+1, i)

        elif depth is limit:
            for i in freqMatrix[depth]:
                if i > cut:
                    result += 1

        else:
            for i in freqMatrix[depth]:
                if i > cut:
                    countSub(freqMatrix, depth+1, i)

    freqMatrix = []

    for char in subSeq:
        freqMatrix.append(findIn(seq, char))

    countSub(freqMatrix, 0, 0)
    print(result)


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        seq, subSeq = line.strip().split(',')
        distSub(seq, subSeq)
