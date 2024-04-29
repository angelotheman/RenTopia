#!/usr/bin/python3
"""
This module defines each item (amenity) found in the apartment
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

class Amenity(Base):
    """
    The table for each amenity which the apartment has
    """

    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(256))
    number = Column(Integer)
    apartment_id = Column(Integer, ForeignKey('apartments.id'))

    apartment = relationship("Apartment", back_populates="amenities")
