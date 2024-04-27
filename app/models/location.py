#!/usr/bin/python3
"""
Module to define the location of appartments
"""
from sqlalchemy import Column, Integer, String
from models import Base


class Location(Base):
    """
    Defining the name and precise locations of the appartments
    """

    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    latitude = Column(String(50))
    longitude = Column(String(50))
