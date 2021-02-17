#!/usr/bin/python3
"""unit test for review"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage


class test_review_class(unittest.TestCase):
    """Unittest for review class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.review = Review()
        print("review object created")

    def test_attr(self):
        """ Tests if class attributes are correct types """
        self.assertIs(self.review.place_id, str())
        self.assertIs(self.review.user_id, str())
        self.assertIs(self.review.text, str())
