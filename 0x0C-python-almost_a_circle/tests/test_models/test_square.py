#!/usr/bin/python3
"""Tests for the square object model"""


import importlib
import models.square
import unittest


Square = models.square.Square


class SquareTests (unittest.TestCase):
    """Tests for the square object model"""

    def setUp(self):
        """Refresh the square module before each test"""

        importlib.reload(models.square)

    def test_InitTooFewArgs(self):
        """Giving too few arguments to the constructor"""

        message = "__init__() missing 1 required positional argument: 'size'"
        with self.assertRaises(TypeError, msg=message):
            Square()

    def test_InitTooManyArgs(self):
        """Giving too many arguments to the constructor"""

        message = "__init__() got an unexpected keyword argument 'ids'"
        with self.assertRaises(TypeError, msg=message):
            Square(5, ids=20)
        message = "__init__() takes from 2 to 5 positional arguments but " \
                  "6 were given"
        with self.assertRaises(TypeError, msg=message):
            Square(1, 2, 3, 4, 5)

    def test_InvalidSize(self):
        """Giving unacceptable values for the square's size"""

        message = "width must be an integer"
        with self.assertRaises(TypeError, msg=message):
            Square('2')
        with self.assertRaises(TypeError, msg=message):
            Square([2])
        s = Square(3)
        with self.assertRaises(TypeError, msg=message):
            s.size = '2'
        with self.assertRaises(TypeError, msg=message):
            s.size = [2]
        message = "width must be > 0"
        with self.assertRaises(ValueError, msg=message):
            Square(-1000)
        with self.assertRaises(ValueError, msg=message):
            Square(0)
        with self.assertRaises(ValueError, msg=message):
            s.size = -1000
        with self.assertRaises(ValueError, msg=message):
            s.size = 0

    def test_SizeUpdatesWidthAndHeight(self):
        """Changing the size and seeing if it changes with and height"""

        s = Square(3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        s.size = 100
        self.assertEqual(s.width, 100)
        self.assertEqual(s.height, 100)

    def test_ToDictionary(self):
        """Converting the object to a dictionary"""

        s = Square(3, 10, 4, 'square')
        d = {'id': 'square', 'size': 3, 'x': 10, 'y': 4}
        self.assertEqual(s.to_dictionary(), d)

    def test_UpdateAttributes(self):
        """Using the update method to change some of the object's attributes"""

        s = Square(3, 10, 4, 'square')
        s.update('changed')
        self.assertEqual(s.id, 'changed')
        s.update('back', 5)
        self.assertEqual(s.id, 'back')
        self.assertEqual(s.size, 5)
        s.update('another', 20, size=30)
        self.assertEqual(s.size, 20)
        s.update('id', 1, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        s.update(y=50)
        self.assertEqual(s.y, 50)
        s.update(id='id2', size=15, x=0, y=1)
        self.assertEqual(s.id, 'id2')
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 1)
        s.update(size=2, y=0, x=10, id=50)
        self.assertEqual(s.id, 50)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 0)
