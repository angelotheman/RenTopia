#!/usr/bin/python3
"""
Defining the business logic for the apartment model
"""
from sqlalchemy.orm import Session
from models.apartment import Apartment


def create_apartment(db: Session, **apartment_data):
    """
    Creates a new apartment in accordance to the models stated
    """
    new_apartment = Apartment(**apartment_data)
    db.add(new_apartment)
    db.commit()
    db.refresh(new_apartment)
    return new_apartment


def update_apartment(db: Session, apartment_id: int, **apartment_data):
    """
    Updates the apartment based on updated information
    """
    apartment = db.query(Apartment).filter(
            Apartment.id == apartment.id).first()

    if not apartment:
        return None

    for key, value in apartment_data.items():
        setattr(apartment, key, value)

    db.commit()
    db.refresh(apartment)
    return apartment


def delete_apartment(db: Session, apartment_id: int):
    """
    Deletes an apartment based on it's id
    """
    if not apartment:
        return False
    db.delete(apartment)
    db.commit()
    return True
