# Reuben Thorpe (2016), CodeEval [Point In Circle v1.0]
from sys import argv
from math import sqrt
import re


def parse_problem(file_path):
    float_regex = re.compile(r"[-+]?\d*\.\d+|[-+]?\d+")

    with open(file_path, "r") as in_file:
        for line in open(argv[1], "r"):
            parse_floats = [float(num) for num in re.findall(float_regex, line)]

            yield({"center": parse_floats[0:2],
                   "radius": parse_floats[2],
                   "point": parse_floats[3:5]})


def distance(x, y):
    """
        Return the distance between two points.
    """

    x1, y1 = x
    x2, y2 = y

    return(sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)))


def is_in_circle(problem):
    """
        Test whether a point is lying within a circle.
    """
    return(distance(problem["center"], problem["point"]) < problem["radius"])


if __name__ == "__main__":
    for problem in parse_problem(argv[1]):
        print("true") if is_in_circle(problem) else print("false")



