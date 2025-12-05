#!/usr/bin/python3
"""Unit tests for the max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_increasing_integers(self):
        """Max should be the last element in a sorted list."""
        numbers = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer(numbers), 10)

    def test_mixed_order_integers(self):
        """Max should be found correctly in an unsorted list."""
        numbers = [10, 1, 7, 3, 9]
        self.assertEqual(max_integer(numbers), 10)

    def test_max_at_start(self):
        """List where the maximum is the first element."""
        numbers = [42, 5, 0, -3]
        self.assertEqual(max_integer(numbers), 42)

    def test_negative_integers(self):
        """List of only negative integers."""
        numbers = [-5, -2, -100, -3]
        self.assertEqual(max_integer(numbers), -2)

    def test_single_element(self):
        """List with a single value should return that value."""
        numbers = [7]
        self.assertEqual(max_integer(numbers), 7)

    def test_empty_list(self):
        """Empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_floats_and_ints(self):
        """List containing both ints and floats."""
        numbers = [1.5, 2, 3.7, 3.6]
        self.assertEqual(max_integer(numbers), 3.7)

    def test_all_equal_values(self):
        """List where all elements are the same."""
        numbers = [4, 4, 4, 4]
        self.assertEqual(max_integer(numbers), 4)

    def test_string_argument(self):
        """Max character in a string is returned (lexicographically)."""
        word = "yara"
        self.assertEqual(max_integer(word), 'y')

    def test_list_of_strings(self):
        """Max string in a list is based on lexicographical order."""
        words = ["apple", "zebra", "mango", "banana"]
        self.assertEqual(max_integer(words), "zebra")

    def test_empty_string(self):
        """Empty string should return None."""
        self.assertIsNone(max_integer(""))

    def test_none_argument(self):
        """Passing None should raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable_argument(self):
        """Passing a non-iterable like an int should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == "__main__":
    unittest.main()
