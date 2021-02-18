#!/usr/bin/python3
"""unit test for base model"""
import unittest
import models
from models.base_model import BaseModel
import os
import json
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# List to store available and known classes
class_list = ["BaseModel", "State", "City", "Amenity", "Place", "Review",
              "User"
              ]
# Dictionary to store available and known classes
class_dict = {"BaseModel": BaseModel,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review,
              "User": User
              }


def remove_file():
    try:
        os.remove("BaseModels.json")
        models.storage.reload()
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
        objs = models.storage._FileStorage__objects
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
        before = models.storage.all()
        models.storage.save()
        self.assertEqual(os.path.isfile("BaseModels.json"), True)
        models.storage.reload()
        after = models.storage.all()
        key = "BaseModel.{}".format(obj.id)
        self.assertEqual(after[key].to_dict(), before[key].to_dict())
        remove_file()

    def test_reload(self):
        """checks if reload is succesful (NOT WORKING)"""
        hold = models.storage.all()
        models.storage.save()
        models.storage.reload()
        after = models.storage.all()
        self.assertCountEqual(models.storage.all(), hold)

    def test_reload_empty_file(self):
        """Test to reload an empty file"""
        before = models.storage.all()
        models.storage.save()
        models.storage.reload()
        after = models.storage.all()
        self.assertEqual(before, after)

    def test_reload_no_file(self):
        """Test to reload no existing file"""
        remove_file()
        self.assertEquals(None, models.storage.reload())

    def test_all(self):
        """TESTS IF ALL() method returns correct type/output"""
        hold = models.storage.all()
        self.assertEqual(type(hold), dict)
        self.assertCountEqual(models.storage.all(), hold)

    def test_all_classes_save(self):
        """Test all classes.save()"""
        for key in class_dict:
            obj = class_dict[key]()
            hold_before = obj.updated_at
            obj.save()
            key = "{}.{}".format(key, obj.id)
            with open("BaseModels.json", mode="r",
                      encoding="utf-8") as file:
                    json_from = json.load(file)
                    self.assertEqual(json_from[key], obj.to_dict())
                    self.assertIn(key, json_from)
            hold_after = obj.updated_at
            self.assertIs(obj.updated_at.__class__, datetime)
            self.assertNotEqual(hold_before, hold_after)
            remove_file()

    def test_save_no_file(self):
        """Trying to save no existent file"""
        with self.assertRaises(TypeError):
            models.storage.save(1)
