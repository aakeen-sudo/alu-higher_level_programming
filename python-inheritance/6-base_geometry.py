#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an unimplemented
area method."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")
