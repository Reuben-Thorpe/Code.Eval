#!/usr/bin/env python3
# Reuben Thorpe (2016), CodeEval [Distinc Triangels v1.0]
"""
 Parts of this code where re-written in python from the link below
 http://www.geeksforgeeks.org/number-of-triangles-in-a-undirected-graph/
"""
from sys import argv
from itertools import product


def get_problem(file_path):
    """
        Parse a single codeeval problem one at a time from the standard
        "testcase.txt" file.
    """
    with open(file_path, "r") as in_file:
        for line in in_file:
            header, connections = line.split(";")
            vertices, edge = [int(i) for i in header.split()]
            lines = tuple(tuple(int(point) for point in connection.split()) for
                          connection in connections.split(","))

            results = {"e": edge, "v": vertices, "lines": lines}
            yield(results)


def convert_to_agj_matrix(vertices, lines):
    """
        Convert vector representation of lines from an undericted graph to an
        adjacency matrix.

    """
    matrix = [[0]*vertices for i in range(vertices)]

    for x in range(vertices):
        for line in lines:
            if x in line:
                x_index = line.index(x)
                y_index = 1 - x_index
                y = line[y_index]
                matrix[x][y] = 1

    return(matrix)


def multiply_square_matrix(matrix_0, matrix_1):
    """
        Multiply square matrices, numpy should be used if speed is a concern.
    """
    dimension = len(matrix_0[0])
    result = [[0]*dimension for i in range(dimension)]

    for i, j in product(range(dimension), range(dimension)):
        for k in range(dimension):
            result[i][j] += matrix_0[i][k]*matrix_1[k][j]

    return(result)


def get_trace(matrix):
    """
        Generate the trace of a matrix.
    """
    dimension = len(matrix[0])
    trace = 0

    for i in range(dimension):
        trace += matrix[i][i]

    return(trace)


def triangles_in_graph(graph):
    """
        Count how many disctinct triangles can be formed from a undirected
        graph in the form of an adjacency matrix.
    """
    aux2 = multiply_square_matrix(graph, graph) # aux2 is graph^2
    aux3 = multiply_square_matrix(graph, aux2)  # aux3 is graph^3

    trace = get_trace(aux3)
    return(trace // 6)


if __name__ == "__main__":
    for problem in get_problem(argv[1]):
        matrix = convert_to_agj_matrix(problem["v"], problem["lines"])
        print(triangles_in_graph(matrix))
