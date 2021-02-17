#!/usr/bin/python3
"""unit test for place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage


class test_place_class(unittest.TestCase):
    """Unittest for place class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.place = Place()
        print("place object created")

    def test_attr(self):
        """ Tests if class attributes are correct types """
        obj = self.place
        self.assertIs(obj.user_id, str())
        self.assertIs(obj.city_id, str())
        self.assertIs(obj.name, str())
        self.assertIs(obj.description, str())
        self.assertIs(obj.number_rooms, int())
        self.assertIs(obj.number_bathrooms, int())
        self.assertIs(obj.max_guest, int())
        self.assertIs(obj.price_by_night, int())
        self.assertIs(type(obj.latitude), float)
        self.assertIs(type(obj.longitude), float)
        self.assertIs(type(obj.amenity_ids), list)
