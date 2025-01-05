#!/usr/bin/python3
"""File storage engine"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File Storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return objects"""
        if cls:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Add new object"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save to file"""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Reload from file"""
        classes = {
            'BaseModel': BaseModel, 'User': User,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Place': Place,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    obj = classes[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete object"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Close storage"""
        self.reload()
