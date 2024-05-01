#!/usr/bin/python3
"""
This module is the abstraction class for operations in the models package
"""
import uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Basemodel:
    """The Basemodel for all other classes"""
    def __init__(self, *var, **vars):
        '''Initialize Base class'''
        self.idd = str(uuid.uuid4())

    def __str__(self) -> str:
        '''To string representation'''
        return f'name: {__class__.__name__}, unique id: {self.idd}'
    
