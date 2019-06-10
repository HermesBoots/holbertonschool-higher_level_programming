#!/usr/bin/python3
"""Base class for all data models"""


import json
import os.path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a JSON string version of list_objs for the given class"""

        if list_objs is None:
            list_objs = []
        list_objs = [b.to_dictionary() for b in list_objs]
        list_objs = cls.to_json_string(list_objs)
        with open(cls.__name__ + '.json', 'wt') as file:
            file.write(list_objs)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string conversion of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) < 1:
            return '[]'
        return json.dumps(list_dictionaries)
