#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage

model = BaseModel()
print("STRING REPRESENTATION OF BASEMODEL")
print(model)

model_json = model.to_dict()
print("JSON SERIALIZATION OF OBJECT")
[print("{}: {}".format(key, model_json.get(key)))
 for key in model_json.keys()]

from_json = BaseModel(**model_json)
from_json.save()

# Reloading saved objects
_objs = storage.all()
[print(value) for key, value in _objs.items()
 if key.split(".")[1] == from_json.id]
