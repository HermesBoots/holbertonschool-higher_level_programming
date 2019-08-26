#!/usr/bin/python3
"""Module to access a search API"""


import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        body = {'q': '""'}
    else:
        body = {'q': sys.argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', body)
    try:
        body = response.json()
    except ValueError:
        print('Not a valid JSON')
    else:
        if hasattr(body, '__contains__') and len(body) < 1:
            print('No result')
        else:
            print('[{}] {}'.format(body['id'], body['name']))
