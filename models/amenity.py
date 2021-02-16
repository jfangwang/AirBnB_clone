#!/usr/python3
"""File contains Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Contains the name of a the desired location or the locations
    of the AirBnb that are in desirable loactions
    Amenity - is something considered to benefit a location, contribute
    to its enjoyment, and thereby increase its value
    Is a empty string at first
    """
    name = ""
