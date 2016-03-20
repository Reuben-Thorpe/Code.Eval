# Reuben Thorpe (2016), CodeEval [Clean Up The Words v1.0]
import re
from sys import argv


def clean_up_words(file_path):
    # Extract words from a string, maintaining word separation and newlines
    in_file = open(file_path, "r").read()
    in_file = re.sub(r"[^a-zA-Z\n]+", ' ', in_file)
    in_file = re.sub(r"\s?\n\s?", '\n', in_file)
    if in_file[0] is not " ":
        return(in_file)
    else:
        return(in_file[1:])


if __name__ == "__main__":
    print(clean_up_words(argv[1]).lower(), end="")




