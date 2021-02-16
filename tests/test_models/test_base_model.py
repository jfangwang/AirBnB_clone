#!/usr/bin/python3
"""unit test for base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """Class test_base"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.mb1 = BaseModel()
        print("mb1 created")

    def test_id(self):
        """tests id of BaseModel instance (makes sure its random)"""
        obj = BaseModel()
        self.assertNotEqual(self.mb1.id, obj.id)  # checks if UUID is unique
        print("{}".format(self.mb1.id))

    def test_str(self):
        """ will test the output of the __str__ magic method """
        obj = self.mb1
        cls_name = obj.__class__.__name__
        self.assertEqual(str(obj),
                         "[{}] ({}) {}".format(cls_name, obj.id, obj.__dict__))

    def test_to_dict(self):
        """ Tests if the format given by to_dict is correct """
        test_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                     'created_at': '2017-09-28T21:03:54.052298',
                     '__class__': 'BaseModel',
                     'my_number': 89,
                     'updated_at': '2017-09-28T21:03:54.052302',
                     'name': 'Holberton'}
        obj = BaseModel(**test_dict)
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict, test_dict)

    def test_time(self):
        """ tests if times are of datetime instance """
        self.assertIs(self.mb1.updated_at.__class__, datetime)
        self.assertIs(self.mb1.created_at.__class__, datetime)

    def test_save(self):
        """ Tests if updated_at changes when save is called """
        before_upd = self.mb1.to_dict()
        self.mb1.save()
        after_upd = self.mb1.to_dict()
        self.assertNotEqual(after_upd["updated_at"], before_upd["updated_at"])

    def test_kwargs(self):
        """ checks if KWARGS properly makes a instance of BaseModel"""
        mb1_dict = self.mb1.to_dict()
        obj = BaseModel(**mb1_dict)
        self.assertEqual(obj.to_dict(), self.mb1.to_dict())
