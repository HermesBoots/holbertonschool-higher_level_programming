#!/usr/bin/python3
"""Wrapper function for isinstance"""


def is_kind_of_class(obj, a_class):
    """Return whether obj is instance of a_class

    Args:
        obj: object to check
        a_class: class to check

    """

    return isinstance(obj, a_class)
