#!/usr/bin/python3
"""
Module for the Review section
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models import Base


class Review(Base):
    """
    This is the table for the review section
    """

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    appartment_id = Column(Integer, ForeignKey('appartments.id'))
    rating = Column(Integer)
    comment = Column(String(256))


    user = relationship("User", back_populates="reviews")
    appartment = relationship("Appartment", back_populates="reviews")
