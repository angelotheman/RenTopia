#!/usr/bin/python
"""
Booking module for the program
"""
from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.base_model import Base


class Booking(Base):
    """
    Table for all bookings made by the user
    """

    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(10))

    user = relationship("User", back_populates="bookings")
    apartment = relationship("Apartment", back_populates="bookings")
