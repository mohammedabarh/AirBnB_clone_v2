#!/usr/bin/python3
"""Test Review class."""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_text(self):
        """Test Review text attribute."""
        review = Review()
        review.text = "Great place!"
        self.assertEqual(review.text, "Great place!")

if __name__ == "__main__":
    unittest.main()
