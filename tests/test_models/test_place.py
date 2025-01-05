#!/usr/bin/python3
"""Test Place Class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self):
        """Set up test cases"""
        self.place = Place()

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test attributes"""
        attributes = [
            'city_id', 'user_id', 'name', 'description',
            'number_rooms', 'number_bathrooms', 'max_guest',
            'price_by_night', 'latitude', 'longitude'
        ]
        for attr in attributes:
            self.assertTrue(hasattr(self.place, attr))

    def test_types(self):
        """Test attribute types"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)


if __name__ == '__main__':
    unittest.main()
