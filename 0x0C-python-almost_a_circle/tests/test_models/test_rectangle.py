#!/usr/bin/python3
"""Tests for rectangle data model"""


import importlib
import models.rectangle
import unittest


Rectangle = models.rectangle.Rectangle


class RectangleTests (unittest.TestCase):
    """Tests for rectangle data model"""

    def setUp(self):
        """Refresh rectangle module before each test"""

        importlib.reload(models.rectangle)

    def test_AttributeValidation(self):
        """Pass various values to attributes that validate input"""

        r = Rectangle(1000, 999, 2000000, 1)
        attrs = ('width', 'height', 'x', 'y')
        good = [1, 2, 3, 4]
        for index, name in enumerate(attrs):
            bad = good.copy()
            bad[index] = '10'
            message = '{} must be an integer'.format(name)
            with self.subTest(name=name, msg='init(\'10\')'):
                with self.assertRaises(TypeError, msg=message):
                    Rectangle(*bad)
            with self.subTest(name=name, msg='r.name = \'10\''):
                with self.assertRaises(TypeError, msg=message):
                    setattr(r, name, '10')
            bad[index] = [10]
            with self.subTest(name=name, msg='init([10])'):
                with self.assertRaises(TypeError, msg=message):
                    Rectangle(*bad)
            with self.subTest(name=name, msg='r.name = [10]'):
                with self.assertRaises(TypeError, msg=message):
                    setattr(r, name, [10])
            bad[index] = -1
            message = '{} must be > 0'.format(name)
            with self.subTest(name=name, msg='init(-1)'):
                with self.assertRaises(ValueError, msg=message):
                    Rectangle(*bad)
            with self.subTest(name=name, msg='r.name = -1'):
                with self.assertRaises(ValueError, msg=message):
                    setattr(r, name, -1)
            if name not in 'xy':
                bad[index] = 0
                with self.subTest(name=name, msg='init(0)'):
                    with self.assertRaises(ValueError, msg=message):
                        Rectangle(*bad)
                with self.subTest(name=name, msg='r.name = 0'):
                    with self.assertRaises(ValueError, msg=message):
                        setattr(r, name, 0)

    def test_InitTooFewArgs(self):
        """Giving the constructor too few arguments"""

        message = "__init__() missing 1 required positional argument: 'height'"
        with self.assertRaises(TypeError, msg=message):
            Rectangle(1)

    def test_InitTooManyArgs(self):
        """Giving the constructor too many arguments"""

        message = '__init__() takes from 3 to 6 positional arguments but 7 ' \
                  'were given'
        with self.assertRaises(TypeError, msg=message):
            Rectangle(1, 2, 3, 4, 5, 6)
