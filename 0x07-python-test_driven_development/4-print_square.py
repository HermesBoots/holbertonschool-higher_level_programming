#!/usr/bin/python3
"""Function to print a square"""


def print_square(size):
    """Print a square consisting of # characters

    Args:
        size (int): length of the sides of the square

    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print('#' * size)
