#!/usr/bin/python3
""" File Storage Module (JSON)"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Contains methods for JSON conversions and file storage """
    __file_path = "BaseModels.json"
    __objects = dict()

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        AKA adds a object to __objects with the key as the above format
        and the value being the dictionary representation of the given object
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        AKA creates JSON representation of __objects and saves it to
        JSON file
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
        """
        json_from = dict()
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                json_from = json.load(file)
        except:
            pass
        
        # ------MAKE BETTER WHY: what happense if name is BASEMODEL
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
