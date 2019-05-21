#!/usr/bin/python3
"""Python source code that produces exact byte code"""
import math


class MagicClass:
    """class to recreate Python byte code"""
    def __init__(self, radius):
        """create new Circle object

        Args:
            radius (int or float): the radius of this circle

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """get this circle's area

        Returns:
            float: this circle's area

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """get this circle's circumference

        Returns:
            float: this circle's circumference

        """
        return 2 * math.pi * self.__radius
