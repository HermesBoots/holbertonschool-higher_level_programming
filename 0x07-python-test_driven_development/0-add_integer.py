#!/usr/bin/python3
"""Function to add two integers"""


def add_integer(a, b=98):
    """Add two integers

    If a or b is a float, the fractional part is truncated before adding.

    Args:
        a (int or float): first operand
        b (int or float: second operand

    Returns:
        int: a + b

    """

    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError('a must be an integer')
    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError('b must be an integer')
    return a + b
