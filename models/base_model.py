#!/usr/bin/python3
"""Base Model File"""
import datetime
import uuid


class BaseModel:
    """Base Model - creates a BaseModel with given data memebers"""
# ----------------------INIT---------------------------------------
    def __init__(self):
        """
        init's public instant attributes:
        > id (str) - unique id assigned ti class object
        > created_at - current datetime of initialization
        > updated_at - current datetime of initialization
        --but will be changed when save() is called
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

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
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()

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
