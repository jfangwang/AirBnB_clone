#!/usr/bin/python3
"""unit test for state"""
import unittest
from models.base_model import BaseModel
from models.state import State

class test_state_class(unittest.TestCase):
    """Unittest for state class"""
    @classmethod
    def setUpClass(cls):
        """Method set up instances"""
        cls.state = State()
        print("state object created")

    def test_attr(self):
        """ Tests if class attributes are correct types """
        self.assertIs(self.state.name, str())
