#!/usr/bin/python3
"""Function to create a list and save it to a file"""


import json
import os.path
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    words = []
    if os.path.exists('add_item.json'):
        words = load_from_json_file('add_item.json')
    words.extend(sys.argv[1:])
    save_to_json_file(words, 'add_item.json')
