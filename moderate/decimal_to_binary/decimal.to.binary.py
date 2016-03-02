# Reuben Thorpe (2016), CodeEval [Decimal To Binary v1.2]
from sys import argv

for line in open(argv[1], 'r'):
    print(bin(int(line))[2:])
