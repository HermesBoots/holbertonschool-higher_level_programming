#!/usr/bin/python3
"""Function to count lines in a file"""


def number_of_lines(filename=""):
    """Return number of lines in file with path given by filename"""

    with open(filename, 'rt', encoding='UTF-8') as file:
        return len(list(file))
