#!/usr/bin/python3

from models.base_model import BaseModel

"""This module defines a User that inherits from Base Model."""


class User(BaseModel):
    """This is a Representation of a User.

    Class Attributes:
        email (str): The user's email
        password (str): The user's password
        first_name (str): The user's first name
        last_name (str): The user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
