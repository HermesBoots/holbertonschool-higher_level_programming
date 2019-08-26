#!/usr/bin/python3
"""Module to read response headers from a web request"""


import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id', ''))
