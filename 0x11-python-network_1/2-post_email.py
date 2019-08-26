#!/usr/bin/python3
"""Module to send data to a web resource"""


import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(
        sys.argv[1],
        b'email=' + sys.argv[2].encode(),
    ) as doc:
        print(doc.read().decode('UTF-8'))
