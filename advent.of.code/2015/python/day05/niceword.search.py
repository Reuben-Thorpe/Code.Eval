# Reuben Thorpe (2015) , Advent of Code 5th December

lookup = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
nicewords = 0
nicewords_2 = 0

data = open("input.txt", "r").read().split()

for word in data:
    # Part1

    if any(i in word for i in lookup):
        continue

    elif sum(word.count(i) for i in vowels) < 3:
        continue

    elif all(word[i] != word[i+1] for i in range(len(word)-1)):
        continue

    nicewords += 1


for word in data:
    # Part 2

    if all(word[i] != word[i+2] for i in range(len(word)-2)):
        continue

    elif all(word.count(str(word[i]+word[i+1])) != 2
             for i in range(len(word)-1)):
        continue

    nicewords_2 += 1


print("\nPart 1 = ", nicewords)
print("Part 2 = ", nicewords_2, "\n")
