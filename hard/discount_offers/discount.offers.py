# -*- coding: ASCII -*-
""" Reuben Thorpe (2015)
HUNGARIAN SOLUTION : OPTIMAL PROFIT ASSIGNMENT
PROOF OF CONCEPT : EXTREMLY UN-OPTIMISED AND NOT READABLE, WILL UPDATE
ONLY IN STD LIBRARY : FASTER WITH NUMPY

 ===== DEBUG NOTES =====

SCORE = 95% [ 1 edge case ]
PROBLEM PROBABLY IN FORMATTING OR SS CALCULATION
TRIED :
        Include y in consonents             : NO
        Don't assume only letters in name   : NO
        Exclude rounding of final ansewr    : NO
        Empty sets                          : YES
"""
from copy import deepcopy
from itertools import product
from fractions import gcd
from sys import argv

VOWELS = "AEIOUYaeiouy"
CONS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"


class hungarian:
    """ Reuben Thorpe (2015)
    I class I created to solve the assignment problem, currently
    in a proof of concept stage, with little to no optimisation
    and a minimum of effort put into readablility, this will be
    improved upon in the future.
    """

    def __init__(self, costMatrix):
        self.M = self._pad(deepcopy(costMatrix))        # Padded copy of input
        self.RM = deepcopy(self.M)                      # Reduced matrix
        self.n = len(self.M)
        self.side = range(self.n)
        self.mValue = 0                                 # Min uncovered value
        self.step = 1                                   # Step command
        self.ZS = [[0]*self.n for i in self.side]       # Stared matrix
        self.ZC = [[0]*self.n for i in self.side]       # Cover matrix
        self.ZP = [[0]*self.n for i in self.side]       # Primes matrix
        self.indicies = []                              # Not implimented!
        self.result = 0                                 # Result!

    def search(self, mode):

        stepMap = ["FINISHED",
                   "self._step1(RM)",
                   "self._step2(RM)",
                   "self._step3()",
                   "self._step4(RM)",
                   "self._step5()",
                   "self._step6(RM)"]

        RM = self.RM
        n = self.n

        if mode == "profit":
            maxRM = max(col for row in RM for col in row)
            RM = [[maxRM - col for col in row] for row in RM]

        while self.step != 0:
            exec(stepMap[self.step])

        # Generates min cost or max profit
        self.result = sum(self.M[x][y] for x, y in
                          product(self.side, self.side) if
                          self.ZS[x][y] == 1)
        return(self.result)

    def _step1(self, matrix):
        """
        For each row of the matrix, find the smallest element and subtract it
        from every element in its row.
        """
        for x, row in enumerate(matrix):
            local_min = min(row)
            for y in self.side:
                matrix[x][y] -= local_min

        self.step = 2

    def _step2(self, matrix):
        """
        Find a zero in the resulting matrix.  If there is no starred zeros
        in its row or column, star Z. Repeat for each element in the matrix.
        """
        lenN = self.side

        for x, y in product(lenN, lenN):
            if matrix[x][y] == 0:
                staredNeigbours = (self.ZS[x][col] == 1 or
                                   self.ZS[row][y] == 1 for
                                   col, row in product(lenN, lenN))

                if not any(staredNeigbours):
                    self.ZS[x][y] = 1

        self.step = 3

    def _step3(self):
        # Needs to be optimised
        """
        Cover each column containing a starred zero.  If n columns are
        covered, the starred zeros describe a complete set of unique
        assignments.
        """
        lenN = self.side

        for x, y in product(lenN, lenN):
            if self.ZS[x][y] == 1:
                for row in lenN:
                    self.ZC[row][y] = 1

        nCover = sum(1 for col in self.ZC[0] if col == 1)

        if nCover == self.n:
            self.step = 0
        else:
            self.step = 4

    def _step4(self, matrix):
        # Needs to be tidied and optimised
        """
        Find a noncovered zero and prime it.  If there is no starred zero in
        the row containing this primed zero, Go to Step 5.  Otherwise, cover
        this row and uncover the column containing the starred zero. Continue
        in this manner until there are no uncovered zeros left. Save the
        smallest uncovered value and Go to Step 6.
        """
        lenN = self.side
        step = 0
        flag = True

        while flag:
            complete = True
            for x, y in product(lenN, lenN):
                if self.ZC[x][y] == 0 and matrix[x][y] == 0:
                    self.ZP[x][y] = 1
                    for col in lenN:
                        if self.ZS[x][col] == 1:
                            self._swap(matrix, x, col)
                            complete = False
                            break
                    if complete:
                        self.step = 5
                        self.Z0 = [x, y]
                        return(0)
                    break
            if complete:
                break

        self.mValue = min(matrix[x][y] for
                          x, y in product(lenN, lenN) if self.ZC[x][y] == 0)
        self.step = 6

    def _step5(self):
        # Needs to be optimised
        """
        Constructs a series of alternating primed and starred zeros as follows.
        Let Z0 represent the uncovered primed zero found in Step 4.
        Let Z1 denote the starred zero in the column of Z0 (if any).
        Let Z2 denote the primed zero in the row of Z1. Continue until the
        series terminates at a primed zero that has no starred zero in its
        column.  Unstar each starred zero of the series, star each primed
        zero of the series, erase all primes and uncover every line in
        the matrix. Returns to Step 3.
        """
        row, col = self.Z0[:]
        complete = False
        Z1 = []
        Z2 = [self.Z0[:]]
        n = 0

        while True:
            for x in self.side:
                if self.ZS[x][col] == 1 and [x, col] not in Z1:
                    Z1 += [[x, col]]
                    row = x
                    break

            for y in self.side:
                if self.ZP[row][y] == 1 and [row, y] not in Z2:
                    Z2 += [[row, y]]
                    col = y
                    break

            if n == len(Z1+Z2):
                break
            else:
                n = len(Z1+Z2)

        for x, y in Z1:
            self.ZS[x][y] = 0

        for x, y in Z2:
            self.ZS[x][y] = 1

        for x, y in product(self.side, self.side):
            self.ZC[x][y] = 0
            self.ZP[x][y] = 0

        self.step = 3

    def _step6(self, matrix):
        """
        Adds the value found in Step 4 to every element of each covered row,
        and subtract it from every element of each uncovered column.
        Returns to Step 4 without altering any stars, primes, or covered lines.
        """
        mValue = self.mValue
        lenN = self.side

        for x in lenN:
            if all(self.ZC[x][y] == 1 for y in lenN):
                for y in lenN:
                    matrix[x][y] += self.mValue

        for y in lenN:
            if any(self.ZC[x][y] == 0 for x in lenN):
                for x in lenN:
                    matrix[x][y] -= self.mValue

        self.step = 4

    def _swap(self, matrix, row, col):
        """
        Uncovers column 'col' and covers row 'row'
        """
        rowLines = [i for i, row in enumerate(self.ZC) if
                    all(col == 1 for col in row)]

        for x in self.side:
            # Check if there are row intersects before deletion
            if x not in rowLines:
                self.ZC[x][col] = 0

        for y in self.side:
            self.ZC[row][y] = 1

    def _pad(self, matrix):
        # Pads a matrix (makes it square by adding zero columns or rows)
        n = len(matrix[0])
        m = len(matrix)
        if m == n:
            return(matrix)

        elif (m < n):
            return(matrix + [[0]*n for i in range(n-m)])

        else:
            return([row + [0]*(m-n) for row in matrix])


def matrixSS(filePath):
    # Produces profit matrices from input file
    results = []
    for line in open(filePath):
        matrixSS = []

        parse_name, parse_item = (section.replace(" ", "").split(",") for
                                  section in line.strip().split(";"))
        try:
            parse_name.remove('')
        except:
            None
        try:
            parse_item.remove('')
        except:
            None

        if parse_item == [] or parse_name == []:
            results += [None]
            continue

        for item in parse_item:
            temp = []
            for name in parse_name:
                temp += [scoreSS(name, item)]
            matrixSS += [temp]

        results += [matrixSS]

    return(results)


def scoreSS(name, item):
        # Produces SS value for customer/product combination
        letter_count = sum(1 for char in item if char in CONS+VOWELS)
        if letter_count % 2 == 0:
            # even
            SS = sum(1.5 for char in name if char in VOWELS)

        else:
            # Not even
            SS = sum(1 for char in name if char in CONS)

        if gcd(len(name), letter_count) != 1:
            # Common factor multiplier
            SS *= 1.5

        return(SS)


if __name__ == "__main__":

    for matrix in matrixSS(argv[1]):
            if matrix is None:
                print("0.00")
            else:
                print("%.2f" % hungarian(matrix).search('profit'))
