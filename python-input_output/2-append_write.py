#!/usr/bin/python3
"""Module that defines a function to append text to a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF8), creating it
    if it doesn't exist.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
