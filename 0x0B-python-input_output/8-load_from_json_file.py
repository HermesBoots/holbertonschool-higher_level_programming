#!/usr/bin/python3
"""Function to load objects from JSON files"""


import json


def load_from_json_file(filename):
    """Return object deserialized from JSON file at path filename"""

    with open(filename, 'rt', encoding='UTF-8') as file:
        return json.load(file)
