#!/usr/bin/python3
"""BaseModel class for all models."""
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class definition."""
    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts instance to dictionary."""
        return {k: v for k, v in self.__dict__.items()}
