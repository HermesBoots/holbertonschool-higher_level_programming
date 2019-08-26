#!/usr/bin/python3
"""Module to send a web request with error handling"""


import sys
import urllib.error
import urllib.request


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as exception:
        print('Error code:', exception.code)
