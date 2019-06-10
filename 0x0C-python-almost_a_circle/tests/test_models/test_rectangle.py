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

    def test_InitTooFewArgs(self):
        """Giving the constructor too few arguments"""

        message = "__init__() missing 1 required positional argument: 'height'"
        with self.assertRaises(TypeError, msg=message):
            Rectangle(1)
