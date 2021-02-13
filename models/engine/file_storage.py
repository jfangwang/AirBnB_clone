#!/usr/bin/python3
""" File Storage Module (JSON)"""
import json


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
                                             obj.id)] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        AKA creates JSON representation of __objects and saves it to
        JSON file
        """
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to FileStorage.__objects again
        AKA creates a python dict from json file and sets it to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except:
            pass
