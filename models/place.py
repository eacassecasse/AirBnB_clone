#!/usr/bin/python3

from models.base_model import BaseModel

"""This module defines a Place that inherits from Base Model."""


class Place(BaseModel):
    """This is a Representation of a Place.

    Class Attributes:
        city_id (str): The identifier of the city
        user_id (str): The user's identifier
        name (str): The name of the place
        description (str): The description shown to the user
        number_rooms (int): The amount of rooms that the place has
        number_bathrooms (int): The amount of bathrooms that the place has
        max_guest (int): The amount of guests supported by the place
        price_by_night (float): The price paid to spend a night at the place
        latitude (float): The latitude coordinate of the place location
        longitude (float): The longitude coordinate of the place location
        amenity_ids (list): The list of amenities of the place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
