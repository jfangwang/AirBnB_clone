#!/usr/bin/python3
"""
Base Model File:
This file contains a class name BaseModel that will serve as the superclass
for data creation of several other classes within the directory
city, state, amenity, place, review, and user...

This file will communicate with the the CWD's __init__.py file to
access a variable called "storage" which contains a instance of our
data engine named file_storage under $PWD/engine/file_storage.py...

More information can be found in the descriptions for both __init__.py
and file_storage.py and how they communicate to the BaseModel class in
this application...
"""
from datetime import datetime  # for update times and creation times
import models  # current module models for access to storage variable from init
import uuid  # imports uuid for unique ID creation


class BaseModel:
    """
    BaseModel:
    BaseModel is a class that sets up basic data members of creation time,
    unique ID's from uuid module, and time of update of data

    Public instance methods:
    __str__() : prints out a BaseModel instance in readable format

    save(): will change class instance update_time and save the
    newly updated instance to a file using applications data engine

    to_dict(): will return a dictionary representation routed from ___dict__
    with additions such as class name and string versions (in ISO) of each
    date time member(public instance attribute).

    __init__(): Uses **kwargs to create or reload a instance of BaseClass

    MORE INFO IN EACH DESCRIPTION============================================
    """

# ----------------------INIT---------------------------------------
    def __init__(self, *args, **kwargs):
        """
        init's public instant attributes:
        > id (str) - unique id assigned t0 class object
        > created_at(datetime) - current datetime of initialization
        > updated_at(datetime) - current datetime of initialization
        but will be update when save() method is called

        If kwargs is empty a standard init is ran with a call to
        module.storage.new(self); which adds the new object to
        FileStorage.__objects; which keeps track of a all object
        created by application. (FileStorage class is loacted in
        engines module under file_storage.py)...

        If kwargs is not empty we will set each class attribute to its
        matching key/value in kwargs. Class is not set since it should
        already be set when __init__ is called based on which class is
        being initialized...
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # updates FileStorage.__objects with new object
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # converts from str back to datetime
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
        the current datetime. Also calles modules.storage.save which
        will save our changed object to FileStorage.__objects dict
        """
        # Updates storage instance before JSON serialization to-
        # -account for changes made during instances active time
        self.updated_at = datetime.now()
        models.storage.save()

# ----------TO_DICT-----------------------------------------
    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        Uses iso.format() built in from datetime module
        will contain all data members associated with the class such
        as User, City, etc along with BaseClass's created_at and updated_at
        members...
        """
        final_dict = dict(self.__dict__)
        # created_at and updated_at are converted to str() iso format
        final_dict["created_at"] = self.created_at.isoformat()
        final_dict["updated_at"] = self.updated_at.isoformat()
        final_dict["__class__"] = self.__class__.__name__
        return final_dict
