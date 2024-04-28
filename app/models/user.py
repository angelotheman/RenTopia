#!/usr/bin/python3
"""
User module for the user table
"""
from sqlalchemy import Column, Integer, String
from models.base_model import Base, Basemodel
import scrypt

class User(Base, Basemodel):
    """
    The class representative of the user table
    """
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    firstname = Column(String(50), index=True, nullable=False)
    lastname = Column(String(50), index=True, nullable=False)
    email = Column(String(128), index=True, nullable=False)
    phone_number = Column(String(10), index=True)
    password = Column(String, nullable=False)

    def __init__(self, *var, **vars):
        '''Initializes the class'''
        super.__init__(*var, **vars)
        if 'password' in vars:
            passcode = vars['password']
            salt = scrypt.gensalt()
            self.password = scrypt.hash(salt, passcode)
