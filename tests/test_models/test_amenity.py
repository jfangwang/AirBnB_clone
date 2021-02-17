#!/usr/bin/python3
"""unit test for amenity"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

class test_amenity_class(unittest.TestCase):
    """Unittest for Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.amenity = Amenity()
        print("amenity object created")

    def test_class(self):
        """ Tests if class is instance of BaseModel and class is State"""
        pass
