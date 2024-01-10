#!/usr/bin/python3

from models.base_model import BaseModel

"""This module defines a City that inherits from Base Model."""


class City(BaseModel):
    """This is a Representation of a City.

    Class Attributes:
        state_id (str): The identifier of the state where the city is
        name (str): The name of the city
    """

    state_id = ""
    name = ""
