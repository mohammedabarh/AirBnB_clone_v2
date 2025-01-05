#!/usr/bin/python3
"""Test User class."""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_email(self):
        """Test User email attribute."""
        user = User()
        user.email = "user@example.com"
        self.assertEqual(user.email, "user@example.com")

if __name__ == "__main__":
    unittest.main()
