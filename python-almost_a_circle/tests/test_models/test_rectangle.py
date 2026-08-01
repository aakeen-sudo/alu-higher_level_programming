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
        r1 = Rectangle(3, 2, id=9)
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

    def test_x_y(self):
        r1 = Rectangle(3, 2, 1, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 5)

    def test_x_default(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2, "1")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 2, -1)

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 1, "5")

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 2, 1, -5)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_perimeter(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.perimeter(), 10)

    def test_str(self):
        r1 = Rectangle(2, 2, 0, 0, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 2/2\n##\n##")

    def test_repr(self):
        r1 = Rectangle(2, 2, 0, 0, 1)
        r2 = eval(repr(r1))
        self.assertEqual(str(r1), str(r2))

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r1.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
