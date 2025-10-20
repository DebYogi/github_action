"""
Unit tests for math operations in src.math_operations.
"""

import unittest
from src.math_operations import add, subtract


class TestMathOperations(unittest.TestCase):
    """Test cases for math operations."""

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        """Test subtraction of two numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)


if __name__ == "__main__":
    unittest.main()
