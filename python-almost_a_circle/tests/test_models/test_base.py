#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_public_facing(self):
        b1 = Base(117)
        self.assertEqual(b1.id, 117)

    def test_default_id(self):
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, b1.id)

    def test_to_json_string(self):
        d = [{"id": 1, "width": 5, "height": 3}]
        s = Base.to_json_string(d)
        self.assertEqual(type(s), str)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        s = '[{"id": 1, "width": 5, "height": 3}]'
        d = Base.from_json_string(s)
        self.assertEqual(d, [{"id": 1, "width": 5, "height": 3}])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])


if __name__ == "__main__":
    unittest.main()
