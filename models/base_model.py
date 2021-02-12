#!/usr/bin/python3
"""Base Model File"""
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Base Model"""
    def __init__(self, id):
        """__init__"""
        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """__str__"""
        return ("[{}] ({}) {}".format(self.__class__.name, self.id, self.__dict__))

    def save(self):
        """save"""
        self.updated_at = datetime.now()

