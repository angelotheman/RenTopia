#!/usr/bin/python3
"""
Routing endpoint for the user model
"""
from fastapi import APIRouter


router = APIRouter(prefix="/users")

# User registration
@router.post("/register")
async def register_user():
    """
    Registers a new user
    """
    pass


# User login
@router.post("/login")
async def login_user():
    """
    Logs in a user
    """
    pass

# Retrieve user profile
@router.get("/profile")
async def get_user_profile():
    """
    Retrieves the user profile
    """
    pass
