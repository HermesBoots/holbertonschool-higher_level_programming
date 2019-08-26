#!/usr/bin/python3
"""Module to download a page with urllib"""


import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()
    print('Body response:')
    print('\t- type:', type(body))
    print('\t- content:', body)
    print('\t- utf8 content:', body.decode('UTF-8'))
