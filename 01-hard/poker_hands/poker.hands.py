# Reuben Thorpe (2016), CodeEval [Poker Hands v1.0]
from collections import defaultdict
from collections import Counter
from copy import deepcopy
from sys import argv


class Hand:
    """
        An abstract class representing a poker hand with various helper
        functions such as "is a hand sequential?".
    """

    def __init__(self, cards):
        self.cards = self._get_type_map(cards)
        self.numbers = self._get_card_numbers()
        self.types = len(self.cards)
        self.groups = list()
        self.counter = Counter()
        self.hand_map = {'High Card': 0, 'One Pair': 1,
                         'Two Pairs': 2, 'Three of a Kind': 3,
                         'Straight': 4, 'Flush': 5,
                         'Full House': 6, 'Four of a Kind': 7,
                         'Straight Flush': 8, 'Royal Flush': 9}


    def _get_type_map(self, cards):
        """
            Map non numeric identifiers into numbers, also organise cards by
            type.
        """
        name_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        hand_map = defaultdict(set)

        for card in cards:
            num, colour = card[0], card[1]

            if num.isdigit():
                hand_map[colour].add(int(num))

            else:
                hand_map[colour].add(name_map[num])

        return(hand_map)


    def _get_card_numbers(self):
        """
            Get all the card numbers from the hand, irespective of type.
        """
        return([num for colr in self.cards.values() for num in colr])


    def min(self):
        """
            Get minimum card number from hand.
        """
        return(min(self.numbers))


    def max(self):
        """
            Get maximum card number from hand.
        """
        return(max(self.numbers))


    def is_sequential(self):
        """
            Test whether the values in a hand are in sequential order.
        """
        card_numbs = set(deepcopy(self.numbers))


        if len(card_numbs) == 5:
            transient = min(card_numbs)
            card_numbs.remove(transient)

            while card_numbs and min(card_numbs) == (transient + 1):
                transient = min(card_numbs)
                card_numbs.remove(transient)

            return(False if card_numbs else True)

        else:
            return(False)


    def n_of_a_kind(self):
        """
            Container for grouping information. How many pairs are there?
        """
        if not self.groups:
            self.counter = Counter(self.numbers)
            self.groups = [i for i in self.counter.values() if i > 1]

        return(self.groups)


    def highest_hand(self):
        """
            Compute the highest possible hand.
        """
        hand_map = self.hand_map

        if self.types == 1:
            if self.is_sequential():
                if self.min() == 10:
                    return(hand_map['Royal Flush'], None)
                else:
                    return(hand_map['Straight Flush'], sum(self.numbers))

            else:
                return(hand_map['Flush'], sum(self.numbers))


        elif self.types == 4 and 4 in self.n_of_a_kind():
            weight = 4 * self.counter.most_common(1)[0][0]
            return(hand_map['Four of a Kind'], weight)


        elif self.is_sequential():
            return(hand_map['Straight'], sum(self.numbers))


        elif self.types >= 3 and 3 in self.n_of_a_kind():
            if 2 in self.n_of_a_kind():
                return(hand_map['Full House'], sum(self.numbers))
            else:
                weight = 3 * self.counter.most_common(1)[0][0]
                return(hand_map['Three of a Kind'], weight)


        elif self.types >= 2 and 2 in self.n_of_a_kind():
            if self.n_of_a_kind().count(2) == 2:
                weight = sum(2*num for num, occ in self.counter.most_common(2))
                return(hand_map['Two Pairs'], weight)
            else:
                weight = 2 * self.counter.most_common(1)[0][0]
                return(hand_map['One Pair'], weight)

        else:
            return(hand_map['High Card'], self.max())


def compare_poker_hands(left_hand, right_hand):
    """
        Compare two poker hand objects and return the one with the highest
        hand.
    """

    l_highest_hand, l_weight = left_hand.highest_hand()
    r_highest_hand, r_weight = right_hand.highest_hand()

    if l_highest_hand > r_highest_hand:
        return('left')

    elif r_highest_hand > l_highest_hand:
        return('right')

    else:
        if l_weight == None:
            return('none')

        elif l_weight > r_weight:
            return('left')

        elif r_weight > l_weight:
            return('right')

        else:
            left_numbers = left_hand.numbers
            right_numbers = right_hand.numbers

            while left_numbers:
                max_l = max(left_numbers)
                max_r = max(right_numbers)

                if max_l > max_r:
                    return('left')

                elif max_r > max_l:
                    return('right')

                else:
                    left_numbers.remove(max_l)
                    right_numbers.remove(max_r)

            return('none')


def parse_problem(file_path):
    """
        Parse the CodeEval problem "Poker Hands".
    """
    with open(file_path, 'r') as in_file:
        for line in in_file:
            line = line.strip()
            if line:
                cards = line.split()
                left_hand = Hand(cards[0:5])
                right_hand = Hand(cards[5:])

                yield(left_hand, right_hand)


if __name__ == '__main__':
    for problem in parse_problem(argv[1]):
        left_hand, right_hand = problem
        print(compare_poker_hands(left_hand, right_hand))
