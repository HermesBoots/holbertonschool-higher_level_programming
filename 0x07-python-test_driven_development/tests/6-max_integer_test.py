#!/usr/bin/python3
"""Tests for the max_integer function"""


import unittest


class TestMaxInt (unittest.TestCase):
    """Class containing tests for max_integer function"""

    extraArgs = 'max_integer() takes from 0 to 1 positional arguments ' \
                'but 2 were given'
    """the error message when extra arguments are given"""
    cantCompare = 'unorderable types: str() > int()'
    """the error message when non-comparable types are used"""
    noLen = 'TypeError: object of type \'int\' has no len()'
    """the error message when an int is passed instead of a collection"""

    def setUp(self):
        """Import the function to test"""
        self.f = max_integer = __import__('6-max_integer').max_integer

    def test_emptyList(self):
        """Test that the function returns nothing with an empty list"""
        self.assertIs(self.f([]), None)

    def test_noArgs(self):
        """Test that the function treats its default argument correctly"""
        self.assertIs(self.f(), None)

    def test_notCollection(self):
        with self.assertRaises(TypeError, msg=self.noLen):
            self.f(2)

    def test_notComparable(self):
        """Test that non-comparable types fail in the right way"""
        with self.assertRaises(TypeError, msg=self.cantCompare):
            self.f(['a', 100, 101])

    def test_numericMix(self):
        """Test that floats and ints can be mixed"""
        self.assertEqual(self.f([3, 4.0, 1, 2.0]), 4.0)

    def test_otherIterable(self):
        """Test that non-list collections still work"""
        tup = tuple("How much wood would a Chuck Quizmo?".split())
        self.assertEqual(self.f(tup), 'would')

    def test_str(self):
        """Test use of function to compare non-numbers"""
        self.assertEqual(self.f(['c', 'b', 'd', 'a']), 'd')

    def test_tooManyArgs(self):
        """Test that giving function too many arguments fails correctly"""
        with self.assertRaises(TypeError, msg=self.extraArgs):
            self.f([], 2)
