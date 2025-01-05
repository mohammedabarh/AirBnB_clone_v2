#!/usr/bin/python3
"""Test User Class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Set up test cases"""
        self.user = User()

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        self.user.email = "test@test.com"
        self.user.password = "test123"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], "test@test.com")
        self.assertEqual(user_dict['password'], "test123")


if __name__ == '__main__':
    unittest.main()
