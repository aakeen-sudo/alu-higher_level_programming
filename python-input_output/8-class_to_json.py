#!/usr/bin/python3
"""Module that defines a function to return a serializable dictionary
representation of a class instance."""


def class_to_json(obj):
    """Return the dictionary description with simple data structures
    for JSON serialization of an object."""
    return obj.__dict__
