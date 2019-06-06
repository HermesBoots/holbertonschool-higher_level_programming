#!/usr/bin/python3
"""Function to print given number of lines from a file"""


def read_lines(filename="", nb_lines=0):
    """Print some lines from a file

    Args:
        filename (str): path to file to print
        nb_lines (int): number of lines to print, counting from the top

    """

    with open(filename, 'rt', encoding='UTF-8') as file:
        if nb_lines <= 0:
            print(file.read(), end='')
            return
        for i, line in zip(range(nb_lines), file):
            print(line, end='')
