#!/usr/bin/python3
"""Function to serialize to JSON"""


import json


def to_json_string(my_obj):
    """Return JSON serialization of my_obj"""

    return json.dumps(my_obj)
