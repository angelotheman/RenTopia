#!/usr/bin/python3
"""
Module for the various appartments in the project
"""
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models import Base


class Appartment(Base):
    """
    This class defines the appartment table based on various appartments
    in the project
    """

    __tablename__ = 'appartments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(256))
    price = Column(Float)
    status = Column(String(50))
    location_id = Column(Integer, ForeignKey('locations.id'))


    location = relationship("Location", back_populates="appartments")
