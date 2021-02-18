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
        models.storage.save()
        self.assertEqual(os.path.isfile("BaseModels.json"), True)
        remove_file()

    def test_reload(self):
        """checks if reload is succesful (NOT WORKING)"""
        hold = models.storage.all()
        models.storage.save()
        models.storage.reload()
        after = models.storage.all()
        self.assertCountEqual(models.storage.all(), hold)

    def test_all(self):
        """TESTS IF ALL() method returns correct type/output"""
        hold = models.storage.all()
        self.assertEqual(type(hold), dict)
        self.assertCountEqual(models.storage.all(), hold)

    def test_key_dict(self):
        """ """
        obj = BaseModel()
        cool = models.storage.all()
        self.assertTrue("BaseModel.{}".format(obj.id) in cool)
        pass
