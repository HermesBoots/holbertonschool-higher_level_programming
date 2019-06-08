#!/usr/bin/python3
"""Base class for all data models"""


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
