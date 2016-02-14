from sys import argv
from itertools import combinations

class assignment:

    def __init__(self):
        self.score = 0  # Running total
        self.S1 = ""    # Shortest sequence
        self.S2 = ""    # Longest sequence

    def score(self, pair):
        """
        Find the alignment score of 2 DNA sequences.
                       Match   : +3
                     Mismatch  : -3
                    Indel start: -8
                     Indel ext : -1
        """
        S1 = self.S1
        S2 = self.S2

        if len(pair[1]) >= len(pair[0]):
            S1, S2 = pair
        else:
            S2, S1 = pair


        return(self.score)

    def _step1(S1, S2):
        pass

    def _score(S1, S3):
        pass



    def _reduce(S1, S2):
        """
        Reduces the problem space by pairing start and end bits.
        S2 is reduced to atleast the size of S1
        """
       pass 













if __name__ == "__main__":
    pairs = (line.strip().replace(" ","").split("|") for line in open(argv[1], 'r'))
    for pair in pairs:
        print(score(pair))









