#!/usr/bin/python3
"""
This module is the abstraction class for operations in the models package
"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Basemodel:
    """The Basemodel for all other classes"""
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))

    def __init__(self, *args, **kwargs):
        '''Initialize Base class'''
        self.id = str(uuid.uuid4())

    def __str__(self) -> str:
        '''To string representation'''
        return f'name: {self.__class__.__name__}, unique id: {self.id}'
    
    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        new_dict["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict
