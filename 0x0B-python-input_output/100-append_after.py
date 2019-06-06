#!/usr/bin/python3
"""Function to insert lines in a file after certain text is found"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new lines in a file after lines with a certain string

    Args:
        filename (str): path to file to edit
        search_string (str): text to trigger insertion of new line
        new_string (str): text to put on newly-inserted lines

    """

    lines = []
    with open(filename, 'rt', encoding='UTF-8') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'wt', encoding='UTF-8') as file:
        file.write(''.join(lines))
