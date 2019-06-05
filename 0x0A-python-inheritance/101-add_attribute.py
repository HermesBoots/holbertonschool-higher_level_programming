#!/usr/bin/python3
"""Class to try adding arbitrary attributes to objects"""


def add_attribute(obj, name, value):
    """Try to assign an attribute on an object if allowed

    Raises:
        TypeError: obj doesn't allow adding attributes called name

    """

    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
