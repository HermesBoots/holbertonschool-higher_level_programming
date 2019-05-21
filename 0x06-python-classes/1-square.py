#!/usr/bin/python3
"""The Square class

Definition of a class that describes a square

"""


class Square:
    """A geometric square

    Contains information about a square and methods for maniuplating it

    """

    def __init__(self, size):
        """Create a square with a given size

        The size of the new square instance is hidden, to be accessed later.

        """

        self.__size = size
