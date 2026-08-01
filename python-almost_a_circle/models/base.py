#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Base class that manages id for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts."""
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from a JSON string."""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
