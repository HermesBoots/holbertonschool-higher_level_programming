#!/usr/bin/python3
"""Module to load a web page using requests"""


import requests


if __name__ == '__main__':
    with requests.get('https://intranet.hbtn.io/status') as response:
        print('Body response:')
        print('\t- type:', type(response.text))
        print('\t- content:', response.text)
