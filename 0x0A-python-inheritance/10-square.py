#!/usr/bin/python3
"""Class with unimplemented method"""


class BaseGeometry:
    """Pseudo-abstract class"""

    def area(self):
        """Not implemented

        Raises:
            NotImplementedError

        """

        raise NotImplementedError('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate an integer argument

        Args:
            name: used in error messages
            value: number to validate

        Raises:
            TypeError: value isn't an integer
            ValueError: value is < 0

        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle (BaseGeometry):
    """A rectangle with just width and height"""

    def __init__(self, width, height):
        """Instantiate a rectangle

        Args:
            width (int): rectangle's width
            height (int): rectangle's height

        """

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return an odd representation of this rectangle"""

        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        """Return this rectangle's area"""

        return self.__width * self.__height


class Square (Rectangle):
    """A square, like a rectangle, but with only one size attribute"""

    def __init__(self, size):
        """Instantiate a new square

        Args:
            size (int): square's side lengths

        """

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return this square's area"""

        return self.__size ** 2
