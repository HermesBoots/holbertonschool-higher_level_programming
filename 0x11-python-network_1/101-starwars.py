#!/usr/bin/python3
"""Module to search for names using the Star Wars API"""


import requests
import sys


if __name__ == '__main__':
    count = 10
    page = 1
    while count == 10:
        response = requests.get(
            'https://swapi.co/api/people/',
            params={'search': sys.argv[1], 'page': page}
        )
        response = response.json()
        results = response.get('results')
        count = len(results)
        if page == 1:
            print('Number of results:', response.get('count'))
        page += 1
        for person in results:
            print(person.get('name'))
