#!/usr/bin/python3
"""Test Amenity Class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Set up test cases"""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        self.amenity.name = "WiFi"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")


if __name__ == '__main__':
    unittest.main()
