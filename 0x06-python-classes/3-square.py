#!/usr/bin/python3
"""The Square class

Definition of a class that describes a square

"""


class Square:
    """A geometric square

    Contains information about a square and methods for maniuplating it

    """

    def __init__(self, size=0):
        """Create a square with a given size

        The size of the new square instance is hidden, to be accessed later.

        Args:
            size (int): length of the square's sides

        Raises:
            TypeError: size argument isn't an integer
            ValueError: size argument is negative

        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Get the area of this square

        Returns:
            the size attribute squared

        """

        return self.__size ** 2
