#!/usr/bin/python3
"""The Square class

Definition of a class that describes a square

"""


class Square:
    """A geometric square

    Contains information about a square and methods for maniuplating it

    """

    @property
    def size(self):
        """int: length of this square's sides

        The setter validates that the size is an integer and is at least 0

        """

        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        if val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def __init__(self, size=0):
        """Create a square with a given size

        The size of the new square instance is hidden, to be accessed later.

        Args:
            size (int): length of the square's sides

        Raises:
            TypeError: size argument isn't an integer
            ValueError: size argument is negative

        """

        self.size = size

    def area(self):
        """Get the area of this square

        Returns:
            the size attribute squared

        """

        return self.__size ** 2
