#!/usr/bin/python3
"""Class to define a student"""


class Student:
    """Represents a serializable student"""

    def __init__(self, first_name, last_name, age):
        """Instantiate a new student with given name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary of serializable attributes of this instance

        Args:
            attrs (list of str): if given, retrieve only the named attributes

        """

        allowed = (list, dict, str, int, bool)
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {
                k: v
                for k, v in self.__dict__.items()
                if isinstance(v, allowed) and k in attrs
            }
        return {k: v for k, v in self.__dict__.items() if type(v) in allowed}
