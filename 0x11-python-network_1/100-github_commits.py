#!/usr/bin/python3
"""Module to retrieve recent GitHub commits for a repository"""


import requests
import sys


if __name__ == '__main__':
    response = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2],
            sys.argv[1]
        )
    )
    for commit in response.json()[:10]:
        line = commit.get('sha')
        line += ': '
        line += commit.get('commit').get('author').get('name')
        print(line)
