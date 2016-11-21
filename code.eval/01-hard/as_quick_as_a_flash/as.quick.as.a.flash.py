# Reuben Thorpe (2016), CodeEval [As Quick As A Flash v1.0]
from sys import argv


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def q_sort_pivots(seq, begin, end):
    """
        Code Evals implimentation of the quick sort algorithm, returns the
        number of pivots enacted during a complete sort.
    """

    if begin < end:
        pivot = seq[begin]
        pivot_pos = begin
        left = begin+1
        right = end

        while left < right:
            while (left < right and seq[right] >= pivot):
                right -= 1

            if seq[right] < pivot:
                swap(seq, pivot_pos, right)
                pivot_pos = right

            if left < right:
                while (left < right and seq[left] <= pivot):
                    left += 1

                if seq[left] > pivot:
                    swap(seq, pivot_pos, left)
                    pivot_pos = left

        return(1 + q_sort_pivots(seq, begin, pivot_pos-1) +
               q_sort_pivots(seq, pivot_pos+1, end))

    else:
        return(0)


if __name__ == "__main__":
    for seq in open(argv[1], "r"):
        seq = [int(num) for num in seq.split()]
        N = len(seq) - 1
        print(q_sort_pivots(seq, 0, N))
