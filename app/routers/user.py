#!/usr/bin/python3
"""
Routing endpoint for the user model
"""
from fastapi import APIRouter


router = APIRouter(prefix="/users")

@router.get("/")
async def home_page():
    return {"message": "FastAPI is up and running"}
