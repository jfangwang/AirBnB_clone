#!/usr/bin/python3
"""sets up unique FileStorage instance for application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
