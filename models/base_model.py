#!/usr/bin/python3
"""Base Model File"""
from datetime import datetime
from models.__init__ import storage
import uuid


class BaseModel:
    """Base Model - creates a BaseModel with given data memebers"""
    def __str__(self):
        """
        human readable __str__: prints [<class name>] (self.id) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime. Also calles storage.save which
        will save our FileStorage.__objects dict (which saves all-
        -of our objects for application) to BaseModels.json
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        Uses iso.format() built in from datetime module
        """
        final_dict = dict(self.__dict__)
        final_dict["created_at"] = self.created_at.isoformat()
        final_dict["updated_at"] = self.updated_at.isoformat()
        final_dict["__class__"] = "BaseModel"
        return final_dict
