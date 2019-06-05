#!/usr/bin/python3
"""Function to get attributes of object"""


def lookup(obj):
    """Return attributes available in object

    Args:
        obj: object to search

    """

    return dir(obj)
