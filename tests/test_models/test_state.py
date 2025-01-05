#!/usr/bin/python3
"""Test State Class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up test cases"""
        self.state = State()

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "California")


if __name__ == '__main__':
    unittest.main()
