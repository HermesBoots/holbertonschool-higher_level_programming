#!/usr/bin/python3
"""Module to search for names using the Star Wars API"""


import requests
import sys


if __name__ == '__main__':
    response = requests.get(
        'https://swapi.co/api/people/',
        params={'search': sys.argv[1]}
    )
    response = response.json()
    print('Number of results:', response.get('count'))
    for person in response.get('results'):
        print(person.get('name'))
