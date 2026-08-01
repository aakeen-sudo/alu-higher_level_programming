#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_empty_list(self):
        """Empty list should return None"""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """No argument uses the default empty list, returns None"""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """List with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_ascending(self):
        """List already sorted ascending"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_descending(self):
        """List already sorted descending"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unordered(self):
        """List in random order"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """Max value is the first element"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max value is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_negative_numbers(self):
        """List of only negative numbers"""
        self.assertEqual(max_integer([-5, -1, -10, -3]), -1)

    def test_mixed_positive_negative(self):
        """List with both positive and negative numbers"""
        self.assertEqual(max_integer([-5, 10, -1, 3]), 10)

    def test_duplicate_max_values(self):
        """List where the max value appears multiple times"""
        self.assertEqual(max_integer([5, 3, 5, 2]), 5)

    def test_all_same_values(self):
        """List where all values are identical"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        """List with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_two_elements(self):
        """List with exactly two elements"""
        self.assertEqual(max_integer([3, 8]), 8)


if __name__ == '__main__':
    unittest.main()