#!/usr/bin/python3
"""Test Amenity class."""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_name(self):
        """Test Amenity name attribute."""
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

if __name__ == "__main__":
    unittest.main()
