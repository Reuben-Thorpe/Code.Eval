# Reuben Thorpe (2016), CodeEval [String List v1.0]
from sys import argv
from itertools import combinations_with_replacement as comb_w_rep
from itertools import permutations


def parse_problem(file_path):
    """
        Parse CodeEval problem sets for String List.
    """
    with open(file_path, 'r') as in_file:
        for line in in_file:
            N, seq = line.strip().replace(' ', '').split(',')
            yield(int(N), set(seq))



if __name__ == '__main__':
    """
        Code golf solution, readability and efficiency are not considered!
    """
    for problem in parse_problem(argv[1]):
        N, string = problem

        comb_generator = (comb for comb in comb_w_rep(string, N))

        perm_set= {perm for comb in comb_generator for
                   perm in permutations(comb)}

        sorted_perm_set = sorted(''.join(perm) for perm in perm_set)

        print(','.join(perm for perm in sorted_perm_set))
