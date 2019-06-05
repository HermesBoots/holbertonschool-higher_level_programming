#!/usr/bin/python3
"""Rebellious int subclass"""


class MyInt (int):
    def __eq__(self, other):
        """Return True if self and other AREN'T equal, False otherwise"""

        return int(self) != other

    def __ne__(self, other):
        """Return True if self and other ARE equal, False otherwise"""

        return int(self) == other
