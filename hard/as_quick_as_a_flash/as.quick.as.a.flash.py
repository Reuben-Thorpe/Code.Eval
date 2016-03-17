# Reuben Thorpe (2016), CodeEval [As Quick As A Flash v1.0]
from sys import argv

def quick_sort_pivots(seq):
    # Returns the number of pivots enacted by the quick sort algorithm
    pivot_count = 0
    N = len(seq) - 1

    def swap(seq, x, y):
        seq[x], seq[y] = seq[y], seq[x]


    def q_sort(seq, begin, end):
        # Code Evals implimentation of the quick sort algorithm
        if begin < end:
            nonlocal pivot_count
            pivot_count += 1
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

            q_sort(seq, begin, pivot_pos-1)
            q_sort(seq, pivot_pos+1, end)

    q_sort(seq, 0, N)
    return(pivot_count)


if __name__ == "__main__":
    for line in open(argv[1], "r"):
        line = [int(num) for num in line.split()]
        print(quick_sort_pivots(line))
