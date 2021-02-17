#!/usr/bin/python3
"""unit test for state"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage

class test_state_class(unittest.TestCase):
    """Unittest for state class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.state = State()
        print("state object created")

    def test_class(self):
        """ Tests if class is instance of BaseModel and class is State"""
        pass
