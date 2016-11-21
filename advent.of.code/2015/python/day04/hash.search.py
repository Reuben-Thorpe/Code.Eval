# Reuben Thorpe (2015) , 4th December

import hashlib
import itertools


lookup = [['1', '00000'], ['2', '000000']]
raw_key = 'bgvyzdsv'

for part, search in lookup:
    for i in itertools.count():
        key = raw_key + str(i)
        hashOutput = hashlib.md5(key.encode('utf-8')).hexdigest()
        if (hashOutput.startswith(search)):
            print("Part", part, " = ", i)
            break
