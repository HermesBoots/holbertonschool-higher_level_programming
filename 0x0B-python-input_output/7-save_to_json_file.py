#!/usr/bin/python3
"""Function to save serialization to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Serialize my_obj and save to a file named by filename"""

    with open(filename, 'wt', encoding='UTF-8') as file:
        json.dump(my_obj, file)
