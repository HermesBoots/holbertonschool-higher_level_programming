#!/usr/bin/python3
"""Tests for rectangle data model"""


import contextlib
import importlib
import io
import models.base
import models.rectangle
import unittest


Rectangle = models.rectangle.Rectangle


class RectangleTests (unittest.TestCase):
    """Tests for rectangle data model"""

    def setUp(self):
        """Refresh rectangle module before each test"""

        importlib.reload(models.base)
        importlib.reload(models.rectangle)

    def test_Area(self):
        """Compare width and height to result of area method"""

        r = Rectangle(200, 500)
        with self.subTest():
            self.assertEqual(r.area(), 100000)
        r.width = 5
        r.height = 1000
        with self.subTest():
            self.assertEqual(r.area(), 5000)

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

    def test_Display(self):
        """Capturing the displayed rectangle"""

        out = io.StringIO()
        r = Rectangle(4, 6)
        result = '####\n####\n####\n####\n####\n####\n'
        with self.subTest():
            with contextlib.redirect_stdout(out):
                r.display()
            self.assertEqual(out.getvalue(), result)
        out.truncate(0)
        out.seek(0)
        r.width = 2
        r.height = 3
        r.x = 3
        r.y = 2
        result = '\n\n   ##\n   ##\n   ##\n'
        with self.subTest():
            with contextlib.redirect_stdout(out):
                r.display()
            self.assertEqual(out.getvalue(), result)

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

    def test_ToString(self):
        """Converting rectangles to a string"""

        r = Rectangle(1, 2, 3, 4)
        result = '[Rectangle] (1) 3/4 - 1/2'
        with self.subTest():
            self.assertEqual(str(r), result)
        r.x = 10
        r.y = 20
        result = '[Rectangle] (1) 10/20 - 1/2'
        with self.subTest():
            self.assertEqual(str(r), result)
        r = Rectangle(5, 6, 7, 8, 9)
        result = '[Rectangle] (9) 7/8 - 5/6'
        with self.subTest():
            self.assertEqual(str(r), result)
        r.width = 30
        r.height = 40
        result = '[Rectangle] (9) 7/8 - 30/40'
        with self.subTest():
            self.assertEqual(str(r), result)
