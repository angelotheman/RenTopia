#!/usr/bin/python3
"""
Module for the various apartments in the project
"""
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models.base_model import Base


class Apartment(Base):
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


    location = relationship("Location", back_populates="apartments")
