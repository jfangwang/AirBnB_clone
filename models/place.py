#!/usr/python3
"""File contains Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class has many different class attributes
    that outline information of our Users place (Airbnb listing)
    """
    city_id = ""  # it will be the City.id of listing
    user_id = ""  # it will be the User.id of owner
    name = ""  # name of place
    description = ""  # description of place
    number_rooms = 0  # Number of rooms listing has
    number_bathrooms = 0  # Number of bathrooms listing has
    max_guest = 0  # Max amount of guests listing can hold
    price_by_night = 0  # Price per night of listing
    latitude = 0.0  # Cords for locations
    longitude = 0.0  # -------------------
    amenity_ids = []  # it will be the list of Amenity.id later
