#!/usr/bin/python3
"""
Module to define the location of appartments
"""
from sqlalchemy import Column, Integer, String, Float
from models import Base


class Location(Base):
    """
    Defining the name and precise locations of the appartments
    """

    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    latitude = Column(Float)
    longitude = Column(Float)
