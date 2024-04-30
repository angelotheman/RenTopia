#!/usr/bin/python3
"""
Module for the various apartments in the project
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, Basemodel
from data_base import data_storage


class Apartment(Base, Basemodel):
    """
    This class defines the appartment table based on various apartments
    in the project
    """

    __tablename__ = 'apartments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(256))
    price = Column(Float)
    status = Column(String(50))
    location_id = Column(Integer, ForeignKey('locations.id'))
    image_path = Column(String)


    location = relationship("Location", back_populates="apartments")
    def __init__(self, *var, **vars):
        '''Initializes the class'''
        super().__init__(*var, **vars)        
