""" Reuben Thorpe (2015) 10th December
This puzzle is an example of Look and Say numbers invented by Jhon Conway.
"""

key = '1113222113'

for i in range(50):
    key = [[char, i+1] for i, char in enumerate(key) if
           i == (len(key)-1) or char != key[(i+1)]]

    key = "".join([str(key[0][1])+key[0][0]] + [str(value[1]-key[i-1][1]) +
                  value[0] for i, value in enumerate(key) if i != 0])

    if i == 39:
        print("Part 1 = ", len(key))

print("Part 2 = ", len(key))
