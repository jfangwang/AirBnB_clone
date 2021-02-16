#!/usr/bin/python3
"""
This File is 1 of 2 files that work as
this applications storage engine (file_storage.py)
and __init__.py in previous directory

Here we have class FileStorage which handles tracking of
current instances of objects while also handling the
Serialization and Deserialization of the applications
objects into and from a JSON file called BaseModels.json(can be modified)
which is created on first run program when objects are created
or saved
"""
import json
# --Imports all classes from models module--
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage: class that handles saving, reloading, and tracking objects

    Class attributes:
    >__file_path: Is the file path in which our .JSON file will be located
        can be modified... is String
    >__objects: Contains all created objects that are reloaded on application
        start or added/modifed in application run time... is Dictionary

    Whenever you create and instance of BaseModel it will be added to
    this __objects Dictionary; This is what module.storage.new() call
    in base_model.py is for; This is also what the module.storage.save()
    is for.

    Public instance methods:
    > all(): returns the dictionary __objects
    > new(): will add a new object to __objects
    > save(): saves __objects to .JSON file... More info in method description
    > reload(): will take .JSON file and turn it back into objects
        for use in application... More info in method description
    """
    __file_path = "BaseModels.json"
    __objects = dict()

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        KEY FORMAT: <obj class name>.id
        sets in __objects the obj with key <obj class name>.id
        AKA adds a object to __objects with the key as the above format
        and the value being the given object
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        AKA creates JSON representation of __objects and saves it to
        JSON file

        Will convert all objects in __objects into thier dictionary repr's
        using to to_dict() method attached to all instanced of BaseClass;
        This is all saved into another dictionary named json_dict
        which is what actually gets serialized; __objects does not get
        serialized only the new json_dict with all of the previous
        objects dictionary representations...

        <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump

        """
        json_dict = dict()
        for key, value in FileStorage.__objects.items():
            json_dict.update({key: value.to_dict()})
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        deserializes the JSON file to FileStorage.__objects again
        AKA creates a python dict from json file and sets it to __objects
        (only if the JSON file (__file_path) exists

        Takes the dictionary of dictionarys that was serialized in save() to
        the .JSON file and creates a dictionary of objects using each
        dicitonary representation of the objects that was deserailzied
        from the file.

        json_from - dictionary of dictionarys taken from file
        (formally json_dict from save())
        > in for loop eahc key value is converted from dict to obj
        > finally __objects is set equal to json_from
            which is now a dict of obj

        At the end of the method __objects will have been restored
        from the json file with data from last run.
        
        JSON load -> <class 'dict'> -> <class 'BaseModel'>
        """
        json_from = dict()
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                json_from = json.load(file)
        except:
            pass

        for key, value in json_from.items():
            if value["__class__"] == "BaseModel":
                json_from[key] = BaseModel(**value)
            elif value["__class__"] == "State":
                json_from[key] = State(**value)
            elif value["__class__"] == "City":
                json_from[key] = City(**value)
            elif value["__class__"] == "Amenity":
                json_from[key] = Amenity(**value)
            elif value["__class__"] == "Place":
                json_from[key] = Place(**value)
            elif value["__class__"] == "Review":
                json_from[key] = Review(**value)
            elif value["__class__"] == "User":
                json_from[key] = User(**value)
        # -----------------------------------------------------------
        FileStorage.__objects = json_from
