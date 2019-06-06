#!/usr/bin/python3
"""Function to append text to a file"""


def append_write(filename="", text=""):
    """Append given text to file with path filename

    Returns:
        int: Number of bytes written

    """

    with open(filename, 'at', encoding='UTF-8') as file:
        return file.write(text)
