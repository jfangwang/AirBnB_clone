#!/usr/bin/python3
"""
sets up unique FileStorage instance for application

storage allows us to use all public instance methods
from FileStorage class (file_stroage.py in engine)
in our BaseClass class to save, load, and add
instances to .json File/__objects(tracking)

Calls reload when program is run because we want
to get all of our saved objects from .JSON file
into our __objects class attribute so we can access
the saved information from those objects
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
