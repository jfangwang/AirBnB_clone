#!/usr/bin/python3
"""Base Model File"""
from datetime import datetime
from models.__init__ import storage
import uuid


class BaseModel:
    """Base Model - creates a BaseModel with given data memebers"""
# ----------------------INIT---------------------------------------
    def __init__(self, *args, **kwargs):
        """
        init's public instant attributes:
        > id (str) - unique id assigned ti class object
        > created_at - current datetime of initialization
        > updated_at - current datetime of initialization
        --but will be changed when save() is called

        if kwargs is empty a standard init is ran with a call to
        storage.new(self) which adds a new object to FileStorage.__objects
        which keeps track of a all object created by application
        (FileStorage class is loacted in engines module under
        file_storage.py)
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)

# ----------STR------------------------------------------------
    def __str__(self):
        """
        human readable __str__: prints [<class name>] (self.id) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

# ----------UPDATE/SAVE----------------------------------------
    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime. Also calles storage.save which
        will save our FileStorage.__objects dict (which saves all-
        -of our objects for application) to BaseModels.json
        """
        self.updated_at = datetime.now()
        storage.save()

# ----------TO_DICT-----------------------------------------
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
