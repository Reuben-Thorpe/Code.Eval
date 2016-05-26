# Reuben Thorpe (2016), CodeEval [Multiplication Tables v1.0]
from sys import argv
import math

# Single line attempt, readability was not the objective!
for num in range(1, 13):
    print("".join((" " * (3 - int(math.log10(num*i)))) + str(num*i) for i in range(1, 13)).strip())
