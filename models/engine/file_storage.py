#!/usr/bin/python3

"""This module defines a file storage class."""
import json
from pathlib import Path


class FileStorage:
    """File Storage Engine.

    This represents an engine for storage management including but
    not limited to JSON Serialization, Deserialization, File Handling.

    Private Class Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): stores all the objects using the
        pattern <class name>.id
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initialize a new File Storage."""

    def all(self):
        """Returns all the objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new object into the list."""
        self.__objects.update({'{}.{}'.format(type(obj).__name__,
                                              obj.id): obj})

    def save(self):
        """Write the JSON serialization of a list of objects to a file."""
        _objects = FileStorage.__objects
        _dict = {key: _objects.get(key).to_dict()
                 for key in _objects.keys()}

        with open(FileStorage.__file_path, "w") as jsonfile:
            if _objects is None or _objects == {}:
                jsonfile.write("{}")
            else:
                jsonfile.write(json.dumps(_dict))

    def reload(self):
        """Deserializes a JSON file"""
        if Path(self.__file_path).is_file():
            with open(file=self.__file_path, mode="r") as jsonfile:
                content = jsonfile.read()
                if content:
                    _dict = json.loads(content)
                    for _obj in _dict.values():
                        class_name = _obj.get('__class__')
                        del _obj['__class__']
                        self.new(eval(class_name)(**_obj))
