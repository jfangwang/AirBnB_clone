#!/usr/bin/python3
"""unit test for base model"""
import unittest
from models.base_model import BaseModel
from models.user import User


class test_user_model(unittest.TestCase):
    """Tests the User class !!!"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.user1 = User()
        print("user1 created")

    def test_attr(self):
        """ Tests if Class attribute values are strings """
        obj = self.user1
        self.assertIs(obj.last_name, str())
        self.assertIs(obj.first_name, str())
        self.assertIs(obj.password, str())
        self.assertIs(obj.email, str())
