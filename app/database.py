#!/usr/bin/python3
"""
Utility functions for the database operations
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config


SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """
    This returns the current database session
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
