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

        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be greater than 0'.format(name))
