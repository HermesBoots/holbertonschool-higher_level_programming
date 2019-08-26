#!/usr/bin/python3
"""Module to post data to a resource with requests"""


import requests
import sys


if __name__ == '__main__':
    response = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(response.text)
