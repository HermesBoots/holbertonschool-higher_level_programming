#!/usr/bin/python3
"""Base class for all data models"""


import json


class Base:
    """Methods and ID tracking used by all persistent classes"""

    __nb_objects = 0
    """Number of objects created with automatic ID"""

    def __init__(self, id=None):
        """Set up object ID, although this class isn't instantiated directly

        Args:
            id: used for object ID if not None; else number of objects used
        
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string conversion of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return '[]'
        return json.dumps(list_dictionaries)
