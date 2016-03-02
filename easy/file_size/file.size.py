# Reuben Thorpe (2016), CodeEval [File Size v1.2]
from sys import argv
import os

byteSize = os.path.getsize(argv[1])
print(byteSize)

