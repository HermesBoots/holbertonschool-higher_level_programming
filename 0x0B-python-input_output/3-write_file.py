#!/usr/bin/python3
"""Function to write to a file"""


def write_file(filename="", text=""):
    """Write given text to file at path filename, destroying its contents"""

    with open(filename, 'wt', encoding='UTF-8') as file:
        return file.write(text)
