#!/usr/bin/python3
"""unit test for city"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage

class test_city_class(unittest.TestCase):
    """Unittest for city class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.city = City()
        print("city object created")

    def test_attr(self):
        """ Tests if class attributes are correct types """
        self.assertIs(self.city.state_id, str())
        self.assertIs(self.city.name, str())
