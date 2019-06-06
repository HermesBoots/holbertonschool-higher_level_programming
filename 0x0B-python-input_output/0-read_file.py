#!/usr/bin/python3
"""Module to cat file"""


def read_file(filename=""):
    """Print contents of file with given filename"""

    with open(filename, 'rt', encoding='UTF-8') as file:
        print(file.read(), end='')
