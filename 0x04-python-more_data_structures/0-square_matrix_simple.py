#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    word a function that computes the square
    value of all integers of a matrix by steve.
    """
    new_matrix = []
    for mat in matrix:
        result = list(map(lambda x: x**2, mat))
        new_matrix.append(result)
    return new_matrix
