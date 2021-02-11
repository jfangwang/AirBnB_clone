#!/usr/bin/python3
"""unit test for base model"""
import unittest
from models.base_model import BaseModel

class test_base_model(unittest.TestCase):
    """Class test_base"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.mb1 = BaseModel()
        print("mb1 created")

    def test_id(self):
        """test id"""
        print("{}".format(self.mb1.id))
