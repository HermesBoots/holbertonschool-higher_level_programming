#!/usr/bin/python3
"""The Square class

Definition of a class that describes a square

"""


class Square:
    """A geometric square

    Contains information about a square and methods for maniuplating it

    """

    @property
    def position(self):
        """tuple of int: the square's position on a plane

        The setter ensures that position is a tuple of 2 positive integers

        """

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integer')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integer')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integer')
        self.__position = value

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

    def __init__(self, size=0, position=(0, 0)):
        """Create a square with a given size and position

        The size of the new square instance is hidden, to be accessed later.

        Args:
            size (int): length of the square's sides

        Raises:
            TypeError: size or position arguments have wrong type
            ValueError: size argument is negative

        """

        self.position = position
        self.size = size

    def __str__(self):
        """Draw square as lines of # characters

        Returns:
            str: representation of the square using rows of # marks

        """

        if self.__size == 0:
            return '\n'
        rows = []
        for _ in range(self.__position[1]):
            rows.append('')
        for _ in range(self.__size):
            rows.append(' ' * self.__position[0] + '#' * self.__size)
        return '\n'.join(rows)

    def area(self):
        """Get the area of this square

        Returns:
            the size attribute squared

        """

        return self.__size ** 2

    def my_print(self):
        """Print out a grid of # representing this square

        Just print a blank line if this size is 0.

        """

        if self.__size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
