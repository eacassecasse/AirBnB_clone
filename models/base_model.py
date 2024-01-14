#!/usr/bin/python3

"""This module defines a Base Model Class."""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """This Represents the base for all other model classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            args (list): (unused) a variable-length list of non-keyword args.
            kwargs (dict): a variable-length dictionary of keyword args
        """
        _format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__.update(
                        {key: datetime.strptime(value, _format)})
                else:
                    self.__dict__.update({key: value})
        else:
            storage.new(self)

    def to_dict(self):
        """Adds new key:value pairs into the BaseModel instance
        dictionary including __class__ which represents the class
        ame and returns this updated dictionary"""
        bm_dict = self.__dict__.copy()
        bm_dict.update({'__class__': self.__class__.__name__})
        bm_dict.update({'created_at': self.created_at.isoformat()})
        bm_dict.update({'updated_at': self.updated_at.isoformat()})

        return bm_dict

    def save(self):
        """Updates the updated_at to the current datetime
        and saves the object into the file"""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
