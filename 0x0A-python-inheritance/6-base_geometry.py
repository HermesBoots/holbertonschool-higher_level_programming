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
