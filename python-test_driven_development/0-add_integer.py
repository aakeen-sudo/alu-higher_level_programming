#!/usr/bin/python3
"""
Module 0-add_integer

Defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers, casting floats to int first.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)