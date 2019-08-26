#!/usr/bin/python3
"""Module to get the ID of an authenticated GitHub user"""


import requests
import sys


if __name__ == '__main__':
    response = requests.get(
        'https://api.github.com/user',
        auth=(sys.argv[1], sys.argv[2])
    )
    print(response.json().get('id'))
