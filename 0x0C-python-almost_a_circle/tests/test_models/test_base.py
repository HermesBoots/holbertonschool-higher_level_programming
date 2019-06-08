#!/usr/bin/python3
"""Tests for data model base class"""


import models.base
import importlib
import unittest


Base = models.base.Base


class BaseTests (unittest.TestCase):
    """Tests for data model base class"""

    def setUp(self):
        """Reset module being tested between tests"""

        importlib.reload(models.base)

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
