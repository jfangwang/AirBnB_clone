#!/usr/bin/python3
"""unit test for place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage

class test_amenity_class(unittest.TestCase):
    """Unittest for place class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.place = Place()
        print("place object created")

    def test_class(self):
        """ Tests if class is instance of BaseModel and class is State"""
        pass
