#!/usr/bin/python3
"""unit test for base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class test_user_model(unittest.TestCase):
    """Tests the User class !!!"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.user1 = User()
        print("user1 created")

    def test_class(self):
        """ Tests if is a class of User and instance of BaseModel"""
        self.assertEqual(self.user1.__class__, User)
        self.assertIsInstance(self.user1, BaseModel)

    def test_kwarg(self):
        """ checks if KWARGS properly makes a instance of BaseModel"""
        usr1_dict = self.user1.to_dict()
        obj = User(**usr1_dict)
        self.assertEqual(obj.to_dict(), self.user1.to_dict())
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.__class__, User)

    def test_str(self):
        """ will test the output of the __str__ magic method """
        obj = self.user1
        cls_name = obj.__class__.__name__
        self.assertEqual(str(obj),
                         "[{}] ({}) {}".format(cls_name, obj.id, obj.__dict__))

    def test_to_dict(self):
        """ Tests if the format given by to_dict is correct """
        test_dict = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
                     "created_at": "2017-09-28T21:11:42.848279",
                     "updated_at": "2017-09-28T21:11:42.848291",
                     "email": "airbnb@holbertonshool.com",
                     "first_name": "Betty", "__class__": "User",
                     "last_name": "Holberton", "password": "root"}
        obj = User(**test_dict)
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict, test_dict)
