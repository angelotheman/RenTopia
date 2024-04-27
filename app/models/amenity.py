#!/usr/bin/python3
"""
This module defines each item (amenity) found in the appartment
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(Base):
    """
    The table for each amenity which the appartment has
    """

    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(256))
    number = Column(Integer)
    appartment_id = Column(Integer, ForeignKey('appartments.id'))

    appartment = relationship("Appartment", back_populates="amenities")
