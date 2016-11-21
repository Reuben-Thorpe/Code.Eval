"""                 --- Reuben Thorpe (2015) ---

The TSP class provides novice solutions to the 'complete and semetric traveling
salsmen problem' for advent of code 2015.

To be added - [held-karp algorithem, monte-carlo simulation]
"""

from itertools import permutations
from time import process_time
import math


class TSP:

    def __init__(self, fileName):
        self.fileName = fileName
        self.data = [line.strip().replace("to", "").replace("=", "").split()
                     for line in open(self.fileName, 'r')]

    def bruteForce(self, **kwargs):
        mode = kwargs.get('mode', None)
        print("\n ---- Initiating brute force with", self.fileName, "----\n")
        distance = []
        positions = list({line[i] for line in self.data for i in range(2)})
        n = len(positions)

        if (mode == 'open'):
            """Solutions for the open ended TSP
            paths start and end at unique nodes
            """
            time = process_time()
            reverseRepeat = (math.factorial(n)/2)

            for i, perm in enumerate(permutations(positions)):
                if i > reverseRepeat:
                    break

                distance.append(sum(int(route[2]) for i in range(n-1) for
                                route in self.data if perm[i] in route and
                                perm[i+1] in route))

        else:
            """Solutions for the standard TSP
            paths start and end at the same node
            """
            time = process_time()
            reverseRepeat = (math.factorial(n-1)/2)
            startPosition = positions[0]

            for i, perm in enumerate(permutations(positions[1:])):
                if i > reverseRepeat:
                    break
                perm = (startPosition,) + perm + (startPosition,)

                distance.append(sum(int(route[2]) for i in range(n) for
                                route in self.data if perm[i] in route and
                                perm[i+1] in route))

        print("Computed minimum : ", min(distance))
        print("Computed maximum : ", max(distance))
        print("Time elapsed (s) : ", (process_time()-time))
        print("   Variation     : ", mode)
        print("  Permutations   : ", len(distance), "\n")


if __name__ == '__main__':
    data = TSP('input.txt')
    # Solutions to Advent of code Day9 (open ended TSP)
    data.bruteForce(mode='open')
    # Solutions to the standard TSP search
    data.bruteForce()
