#!/usr/bin/python3
"""Add method to list class"""


class MyList (list):
    """Class to add extension method to list"""

    def print_sorted(self):
        """Print the list like normal, but elements are sorted"""

        print(sorted(self))
