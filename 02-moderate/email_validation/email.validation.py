# Reuben Thorpe (2016), CodeEval [Email Validation v1.0]
from sys import argv
import re


regex_match_string = r'^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}'

with open(argv[1], "r") as in_file:
    email_validation = re.compile(regex_match_string)

    for email_string in in_file:
        if email_string:
            print("true") if re.match(email_validation, email_string) else print("false")
