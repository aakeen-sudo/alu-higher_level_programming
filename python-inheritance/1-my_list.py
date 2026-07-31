#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """A list subclass with a method to print elements in sorted order."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))
