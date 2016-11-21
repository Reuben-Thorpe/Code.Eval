# Reuben Thorpe (2016), CodeEval [Valid Parentheses v1.1]
from sys import argv
import re


with open(argv[1], 'r') as in_file:
    parentheses_regex = re.compile('\(\)|\[\]|\{\}')
    valid_parentheses = {'{}', '()', '[]'}


    for line in in_file:
        line = line.strip()

        while re.findall(parentheses_regex, line):
            for pair in valid_parentheses:
                line = line.replace(pair, '')

        print(not line)
