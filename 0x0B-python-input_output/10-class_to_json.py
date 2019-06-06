#!/usr/bin/python3
"""Function to get dict of JSON-serializable attributes of an object"""


def class_to_json(obj):
    """Return dict containing JSON-serializable attributes of obj"""

    allowed = (list, dict, str, int, bool)
    return {k: v for k, v in obj.__dict__.items() if isinstance(v, allowed)}
