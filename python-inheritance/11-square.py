#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle,
with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inheriting area and validation from
    Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        w = self._Rectangle__width
        h = self._Rectangle__height
        return "[Square] {}/{}".format(w, h)
