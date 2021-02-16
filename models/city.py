#!/usr/python3
"""File contains City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Has only two class attributes both empty strings
    state_id = empty string but will be filled with state_id
    name = empty string but will be name of city
    """
    state_id = ""
    name = ""
