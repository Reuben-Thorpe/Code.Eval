# Reuben Thorpe (2016), String Search
from sys import argv


def check(string, second):
    # Checks if second is in string, with regular expression "*"

    if "*" not in second:
        # Standard search
        return(compare(string, second))

    else:
        # Found regex or escaped "*" char

        if "\\*" in second:
            if second.count("\\*") == second.count("*"):
                # Found only escape char
                second = second.replace("\\*", "*")
                return(compare(string, second))
            else:
                # Found escape with regex
                index = [i for i, char in enumerate(second) if char == "*" and
                         second[abs(i-1)] != "\\"]

                start = 0
                second_strings = []
                for i in index:
                    second_strings += [second[start:i].replace("\\*", "*")]
                    start = i+1

                second_strings += [second[start:].replace("\\*", "*")]
                return(compareR(string, second_strings))

        else:
            # Found only regex
            second = second.split("*")
            return(compareR(string, second))


def compare(string, second):
    if second in string:
        return("true")
    else:
        return("false")


def compareR(string, second_strings):
    # Compare with regex
    index = 0
    for second in second_strings:
        if second not in string[index:]:
            return("false")
        index += len(second)
    return("true")


if __name__ == "__main__":
    parse = (line.strip().split(",") for line in open(argv[1], "r"))

    for string, second in parse:
        print(check(string, second))
