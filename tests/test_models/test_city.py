#!/usr/bin/python3
"""Test City class."""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def test_name(self):
        """Test City name attribute."""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

if __name__ == "__main__":
    unittest.main()
