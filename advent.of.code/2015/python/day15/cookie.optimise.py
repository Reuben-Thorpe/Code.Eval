# Reuben Thorpe (2015) , Advent of Code 2015  15th of December
# NOTE : replace test parse with regex

from itertools import combinations_with_replacement
from string import ascii_lowercase as alpha
from operator import mul

nTeaspoons = 100


def part1(fileName):
    ingredientStat = {i: [int(n) for
                      n in [line[2], line[4], line[6], line[8]]] for
                      i, line in zip(alpha, [line.replace(",", "").split() for
                                             line in open(fileName)])}

    key = alpha[:len(ingredientStat)]
    combinations = []

    for comb in combinations_with_replacement(key, nTeaspoons):
        temp = []

        for ingredient in key:
            n = comb.count(ingredient)
            temp += [[n*value for value in ingredientStat[ingredient]]]

        temp = [temp[0][i] + temp[1][i] + temp[2][i] + temp[3][i] for
                i in range(4)]

        if not any([True for i in temp if i <= 0]):
            combinations += [temp[0]*temp[1]*temp[2]*temp[3]]

        print("Part 1 = ", max(combinations))


def part2(fileName):
    ingredientStat = {i: [int(n) for
                      n in [line[2], line[4], line[6], line[8], line[10]]] for
                      i, line in zip(alpha, [line.replace(",", "").split() for
                                             line in open(fileName)])}

    key = alpha[:len(ingredientStat)]
    combinations = []

    for comb in combinations_with_replacement(key, nTeaspoons):
        temp = []

        for ingredient in key:
            n = comb.count(ingredient)
            temp += [[n*value for value in ingredientStat[ingredient]]]

        temp = [temp[0][i] + temp[1][i] + temp[2][i] + temp[3][i] for
                i in range(5)]

    if not any([True for i in temp if i <= 0]):
        if temp[4] == 500:
            combinations += [temp[0]*temp[1]*temp[2]*temp[3]]

    print("Part 2 = ", max(combinations))


part1('input.txt')
part2('input.txt')
