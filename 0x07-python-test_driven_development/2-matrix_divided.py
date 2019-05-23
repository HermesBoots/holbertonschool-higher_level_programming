#!/usr/bin/python3
"""Function to divide all numbers in a matrix"""


def matrix_divided(matrix, div):
    """Get new matrix by dividing all items in it by a given number

    Args:
        matrix (list of list of (int or float)): matrix of numbers to divide
        div (int or float): number to divide each item in the matrix by

    Returns:
        list of list of float: matrix with same dimensions where each number is
        divided by div

    """

    message = 'matrix must be a matrix (list of lists) of integers/floats'
    isita = isinstance
    if not isita(matrix, list):
        raise TypeError(message)
    if not all(isita(i, list) for i in matrix):
        raise TypeError(message)
    if not all(isita(i, int) or isita(i, float) for l in matrix for i in l):
        raise TypeError(message)
    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isita(div, int) and not isita(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[i / div for i in l] for l in matrix]
