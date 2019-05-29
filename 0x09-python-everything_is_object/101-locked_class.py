#!/usr/bin/python3
"""Class that restrcits attribute assignment"""


class LockedClass:
    """Simple class that only allows assigning attributes named first_name"""

    __slots__ = ('first_name',)
    """The attribute that limits other attribute creation"""
