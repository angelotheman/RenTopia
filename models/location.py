#!/usr/bin/python3
"""
Module to define the location of apartments
"""
from sqlalchemy import Column, Integer, String, Float
from models.base_model import Base, Basemodel


class Location(Base,Basemodel):
    """
    Defining the name and precise locations of the apartments
    """

    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    def __init__(*var, **vars):
        super.__init__(*var, **vars)
