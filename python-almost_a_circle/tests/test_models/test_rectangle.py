#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_width_height(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)

    def test_id_inherited(self):
        r1 = Rectangle(3, 2, 9)
        self.assertEqual(r1.id, 9)

    def test_width_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle("3", 2)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "2")

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(3, -2)


if __name__ == "__main__":
    unittest.main()
