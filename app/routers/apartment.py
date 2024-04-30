#!/usr/bin/python3
"""
The end point routes for apartments
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models.apartment import Apartment
from database import get_session
from services.apartment import create_apartment
from services.apartment import update_apartment, delete_apartment


router = APIRouter(prefix="/apartments")


@router.get("", response_model=List[Apartment])
async def get_apartments(db: Session = Depends(get_session)):
    """
    Get all the appartments from the database
    """

    apartments = db.query(Apartment).all()
    return apartments


@router.get("/{apartment_id}")
async def get_appartment_by_id(apartment_id: int,
                               db: Session = Depends(get_session)):
    """
    Gets a particular apartment
    """
    return {"message": "FastAPI is up and running"}

    apartment = db.query(Apartment).filter(
            Apartment.id == apartment_id).first()

    if apartment is None:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return apartment


@router.post("/create_apartment", response_model=Apartment)
async def create_apartment(apartment_data: dict,
                           db: Session = Depends(get_session)):
    """
    Endpoint for creating an apartment
    """
    new_apartment = create_apartment(db, **apartment_data)
    return new_apartment


@router.put("/{apartment_id}", response_model=Apartment)
async def update_apartment(apartment_id: int, apartment_data: dict,
                           db: Session = Depends(get_session)):
    """
    Updates an appartment information
    """
    updated_apartment = update_apartment(db, apartment_id, **apartment_data)

    if updated_apartment is None:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return updated_apartment


@router.delete("/{apartment_id}")
async def delete_apartment(apartment_id: int,
                           db: Session = Depends(get_session)):
    """
    Deletes an apartment
    """
    success = delete_apartment(db, apartment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Apartment not found")
    return {"message": "Apartment deleted successfully"}
