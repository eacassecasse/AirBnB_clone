#!/usr/bin/python3

from models.base_model import BaseModel

"""This module defines a Review that inherits from Base Model."""


class Review(BaseModel):
    """This is a Representation of a Review.

    Class Attributes:
        place_id (str): The place being reviewed
        user_id (str): The identifier of the user who reviews
        text (str): The review message written by the user
    """

    place_id = ""
    user_id = ""
    text = ""
