#!/usr/bin/python3
"""Module that defines a function to convert a JSON string into an
object (Python data structure)."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string."""
    return json.loads(my_str)
