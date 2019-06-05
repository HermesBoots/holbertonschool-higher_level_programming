#!/usr/bin/python3
"""Module with version of isinstance that ignores inheritence"""


def is_same_class(obj, a_class):
    """Find if object is a member of a class, not one of its ancestors

    Args:
        obj: instance to check
        a_class: class to check

    Returns:
        bool: True if obj is instance of a_class, else False

    """

    return type(obj) is a_class
