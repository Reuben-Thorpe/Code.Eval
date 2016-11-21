# Reuben Thorpe (2015) , 3rd December Advent of Code

ledger_1 = [[0, 0]]
ledger_2 = [[0, 0]]
santa_position_1 = [0, 0]
santa_position_2 = [0, 0]
robot_position_2 = [0, 0]
santa = True


def move(i, ledger, position):
    if i == "^":
        position[0] += 1
    elif i == "v":
        position[0] -= 1
    elif i == ">":
        position[1] += 1
    else:
        position[1] -= 1

    if position not in ledger:
        ledger.append([position[0], position[1]])

    return(position)

data = open('input.txt', 'r').read().strip()

for i in data:
    santa_position_1 = move(i, ledger_1, santa_position_1)

    if santa:
        santa_position_2 = move(i, ledger_2, santa_position_2)
        santa = False
    else:
        robot_position_2 = move(i, ledger_2, robot_position_2)
        santa = True


print("\nPart 1 = ", len(ledger_1))
print("Part 2 = ", len(ledger_2), "\n")
