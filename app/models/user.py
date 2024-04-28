#!/usr/bin/python3
"""
User module for the user table
"""
from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    """
    The class representative of the user table
    """
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    firstname = Column(String(50), index=True)
    lastname = Column(String(50), index=True)
    email = Column(String(128), index=True)
    phone_number = Column(String(10), index=True)
