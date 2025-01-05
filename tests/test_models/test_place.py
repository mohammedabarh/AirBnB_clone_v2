#!/usr/bin/python3
"""Test Place class."""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_name(self):
        """Test Place name attribute."""
        place = Place()
        place.name = "Room"
        self.assertEqual(place.name, "Room")

if __name__ == "__main__":
    unittest.main()
