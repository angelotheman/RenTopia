#!/usr/bin/python3
"""
User module for the user table
"""
from sqlalchemy import Column, Integer, String
from models import Base


class User(Base):
    """
    The class representative of the user table
    """
    __tablename__ = 'users'

    id = Column(String)