#!/usr/bin/python3
"""unit test for base model"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage

class test_base_model(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        set_dict = {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381",
         "created_at": "2017-09-28T21:07:25.047372", "name": "Holberton", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}
        
        cls.mb2 = BaseModel(**set_dict)
        print("\nmb2 created\n")

    def test_save(self):
        """ """
        self.mb2.save()
        print("saved")

    def test_reload(self):
        """ """
        pass

    def test_json(self):
        """ """
        pass
