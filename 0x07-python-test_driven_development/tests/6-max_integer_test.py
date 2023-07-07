#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_with_string(self):
        """test with string"""
        string = "Brain"
        self.assertEqual(max_integer(string), 'r')

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element = [5]
        self.assertEqual(max_integer(single_element), 5)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 17.5, -19, 16, 7]
        self.assertEqual(max_integer(ints_and_floats), 17.5)

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "3"])
        self.assertRaises(TypeError, max_integer, [1, 2, None])
        self.assertRaises(TypeError, max_integer, [1, 2, [3]])

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Feyi", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([-2, -2, -2, -2, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)
        self.assertEqual(max_integer([1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, -1, 1, -1, -1]), 1)


if __name__ == '__main__':
    unittest.main()
