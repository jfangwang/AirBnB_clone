#!/usr/python3
"""File contains User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """contains user profile data in class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
