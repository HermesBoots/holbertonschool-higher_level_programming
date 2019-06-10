#!/usr/bin/python3
"""Tests for data model base class"""


import importlib
import json
import models.base
import models.rectangle
import models.square
import os
import unittest


Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


class BaseTests (unittest.TestCase):
    """Tests for data model base class"""

    def setUp(self):
        """Reset module being tested between tests"""

        importlib.reload(models.base)
        importlib.reload(models.rectangle)
        importlib.reload(models.square)

    def test_InitTooManyArgs(self):
        "Passing too many constructor arguments"""

        message = '__init__() takes from 1 to 2 positional arguments but 3 ' \
                  'were given'
        with self.assertRaises(TypeError, msg=message):
            Base(1, 2)

    def test_InitDefaultId(self):
        """Passing no arguments to the constructor"""

        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj.id, 1)
        obj3 = Base('not none')
        self.assertNotEqual(obj3.id, 3)
        obj4 = Base()
        self.assertEqual(obj4.id, 3)

    def test_InitGivenId(self):
        """Passing a desired ID to the constructor"""

        obj = Base('str')
        self.assertEqual(obj.id, 'str')
        obj = Base(1000)
        self.assertEqual(obj.id, 1000)
        obj = Base([1, 2, 3])
        self.assertEqual(obj.id, [1, 2, 3])
        obj = Base(None)
        self.assertEqual(obj.id, 1)

    def test_Save(self):
        """Saving JSON to a file"""

        try:
            os.remove('Rectangle.json')
        except FileNotFoundError:
            pass
        try:
            os.remove('Square.json')
        except FileNotFoundError:
            pass
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        j = json.dumps([r1.to_dictionary(), r2.to_dictionary()])
        with self.subTest():
            Rectangle.save_to_file([r1, r2])
            with open('Rectangle.json', 'rt') as file:
                self.assertEqual(file.read(), j)
        with self.subTest():
            Rectangle.save_to_file(None)
            with open('Rectangle.json', 'rt') as file:
                self.assertEqual(file.read(), '[]')
        s1 = Square(10, 20, 30)
        s2 = Square(100, 200, 300)
        j = json.dumps([s1.to_dictionary(), s2.to_dictionary()])
        with self.subTest():
            Square.save_to_file([])
            with open('Square.json', 'rt') as file:
                self.assertEqual(file.read(), '[]')
        with self.subTest():
            Square.save_to_file([s1, s2])
            with open('Square.json', 'rt') as file:
                self.assertEqual(file.read(), j)

    def test_ToJson(self):
        """Converting a list to a JSON representation"""

        with self.subTest():
            self.assertEqual(Base.to_json_string(None), '[]')
        with self.subTest():
            self.assertEqual(Base.to_json_string([]), '[]')
        b = Base()
        j = [{'a': 1, 'b': 2}, {1: 'a', 2: 'b'}]
        with self.subTest():
            self.assertEqual(b.to_json_string(j), json.dumps(j))
        with self.subTest():
            self.assertEqual(Base.to_json_string(j), json.dumps(j))
