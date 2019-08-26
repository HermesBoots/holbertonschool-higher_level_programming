#!/usr/bin/python3
"""Module to read resonse header from a web page"""


import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
