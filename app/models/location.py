#!/usr/bin/python3
"""
Module to define the location of apartments
"""
from sqlalchemy import Column, Integer, String, Float
from models.base_model import Base


class Location(Base):
    """
    Defining the name and precise locations of the apartments
    """

    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    latitude = Column(Float)
    longitude = Column(Float)
