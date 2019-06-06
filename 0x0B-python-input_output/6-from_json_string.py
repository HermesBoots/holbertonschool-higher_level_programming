#!/usr/bin/python3
"""Function to deserialize JSON strings"""


import json


def from_json_string(my_str):
    """Return deserialization of my_str using JSON"""

    return json.loads(my_str)
