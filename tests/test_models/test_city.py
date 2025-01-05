#!/usr/bin/python3
"""Test City Class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Set up test cases"""
        self.city = City()

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        self.city.name = "San Francisco"
        self.city.state_id = "CA"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['state_id'], "CA")


if __name__ == '__main__':
    unittest.main()
