#!/usr/bin/python3
"""Function to print a line split into paragraphs"""


def text_indentation(text):
    """Split the text into paragraphs

    Paragraphs end at a ':', '.', or '?' character. After one is found, two
    line breaks are added. Paragraphs don't start or end with spaces.

    Args:
        text (str): text to split

    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    paras = []
    last = 0
    for i, c in enumerate(text):
        if c in '.:?':
            paras.append(text[last:i+1].strip())
            last = i + 1
    if last <= len(text):
        paras.append(text[last:].strip())
    print('\n\n'.join(paras), end='')
