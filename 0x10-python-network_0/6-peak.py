#!/usr/bin/python3
"""Module to find a peak in a list of numbers"""


def find_peak(list_of_integers):
    """Find a peak in a list of integers"""

    if len(list_of_integers) < 1:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    ints = list_of_integers
    gap = len(ints) // 2
    index = gap - 1
    while gap > 0:
        if (
            (index == 0 and ints[index] > ints[index + 1]) or
            (index == len(ints) - 1 and ints[index] > ints[index - 1]) or
            (ints[index] > ints[index - 1] and ints[index] > ints[index + 1])
        ):
            return ints[index]
        gap = (gap + 1) // 2 if gap > 1 else 0
        if index < len(ints) - 1 and ints[index + 1] > ints[index]:
            index += gap
        else:
            index -= gap
    return ints[index]
