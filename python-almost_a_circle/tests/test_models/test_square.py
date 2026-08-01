#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_x_y_id(self):
        s1 = Square(5, 1, 2, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 3)

    def test_area(self):
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_str(self):
        s1 = Square(5, 1, 1, 3)
        self.assertEqual(str(s1), "[Square] (3) 1/1 - 5")

    def test_size_not_int(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-5)


if __name__ == "__main__":
    unittest.main()
