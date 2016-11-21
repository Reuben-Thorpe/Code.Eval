# Reuben Thorpe (2015), 21st December Advent of Code

import itertools


class RPG:
    """ RPG Simulator 20XX

     Shop stat format   = [GOLD, DAMAGE, ARMOR]
    Player stat format  = [HEALTH, DAMAGE, ARMOR]

    """
    weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0],
               [74, 8, 0]]

    armor = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4],
             [102, 0, 5], [0, 0, 0]]

    rings = {"DMG 1": [25, 1, 0],
             "DMG 2": [50, 2, 0],
             "DMG 3": [100, 3, 0],
             "DEF 1": [20, 0, 1],
             "DEF 2": [40, 0, 2],
             "DEF 3": [80, 0, 3],
             "EMPTY": [0, 0, 0]}

    player_max_health = 100
    part_1 = []
    part_2 = []

    def __init__(self, fileName):
        # Parse bosses input stats [Input to AoC]
        data = [line.split() for line in open(fileName, "r")]
        self.boss = [int(line[-1:][0]) for line in data]

    def search(self):
        # Searches for optimal inventory
        ring_comb = ([i for i in itertools.combinations(RPG.rings, 2)] +
                     [('EMPTY', 'EMPTY')])

        for inv in itertools.product(RPG.weapons, RPG.armor, ring_comb):

            gold = (inv[0][0] + inv[1][0] + RPG.rings[inv[2][0]][0] +
                    RPG.rings[inv[2][1]][0])

            player_atk = (inv[0][1] + RPG.rings[inv[2][0]][1] +
                          RPG.rings[inv[2][1]][1])

            player_def = (inv[1][2] + RPG.rings[inv[2][0]][2] +
                          RPG.rings[inv[2][1]][2])

            if (player_def - self.boss[1]) >= 0:
                boss_atk = 1
            else:
                boss_atk = -(player_def-self.boss[1])
            if (self.boss[2] - player_atk) >= 0:
                player_atk = 1
            else:
                player_atk = -(self.boss[2] - player_attack)

            # Part 1
            if (RPG.player_max_health/boss_atk) > (self.boss[0]/player_atk):
                RPG.part_1 += [gold]

            # Part 2
            else:
                RPG.part_2 += [gold]

        print("\nPart 1 = ", min(RPG.part_1))
        print("Part 2 = ", max(RPG.part_2), "\n")

if __name__ == '__main__':

    RPG('input.txt').search()
