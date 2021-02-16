#!/usr/python3
"""Hold class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review information for a users listing/profile"""
    place_id = ""  # Place identifaction number
    user_id = ""  # the id of the User profile
    text = ""  # The review...
