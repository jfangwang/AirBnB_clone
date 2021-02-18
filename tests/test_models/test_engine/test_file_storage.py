#!/usr/bin/python3
"""unit test for base model"""
import unittest
import models
from models.base_model import BaseModel
import os


def remove_file():
    try:
        os.remove("BaseModels.json")
    except:
        pass

class test_file_storage(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        remove_file()
        print("setup")

    def tearDown(self):
        """ Remove storage file at end of tests """
        remove_file()

    def test_file_path(self):
        """ checks if file_path is a string """
        path = models.storage._FileStorage__file_path
        self.assertEqual(type(path), str)

    def test_file_objects(self):
        """ checks if __objects is a dict """
        objs = models.storage.all()
        self.assertEqual(type(objs), dict)

    def test_new(self):
        """ """
        obj = BaseModel()
        dict_obj = models.storage.all()
        self.assertEqual(dict_obj["BaseModel.{}".format(obj.id)], obj)
        self.assertTrue(dict_obj["BaseModel.{}".format(obj.id)] is obj)
        remove_file()

    def test_save(self):
        """Checks if save is succesful"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        obj.save()
        self.assertEqual(os.path.isfile("BaseModels.json"), True)
        remove_file()

    def test_reload(self):
        """ """
        pass

    def test_all(self):
        """ """
        pass

    def test_serial(self):
        """ """
        pass
