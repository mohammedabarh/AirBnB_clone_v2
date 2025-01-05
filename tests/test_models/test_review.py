#!/usr/bin/python3
"""Test Review Class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Set up test cases"""
        self.review = Review()

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """Test to_dict method"""
        self.review.text = "Great place!"
        self.review.user_id = "user123"
        self.review.place_id = "place123"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['text'], "Great place!")
        self.assertEqual(review_dict['user_id'], "user123")
        self.assertEqual(review_dict['place_id'], "place123")


if __name__ == '__main__':
    unittest.main()
