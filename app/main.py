#!/usr/bin/python3
"""
This is the entry point of the entire application
"""
from fastapi import FastAPI
from routers import user, apartment, booking, review
#from database import engine
#from models.base_model import Base


app = FastAPI()


# Include routers
app.include_router(user.router)
#app.include_router(apartment.router)
#app.include_router(booking.router)
#app.include_router(review.router)


# Create tables
#Base.metadata.create_all(bind=engine)
