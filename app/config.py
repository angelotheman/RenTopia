#!/usr/bin/python3
"""
Module to define the particulars of my configuration settings
"""
import os


class Config:
    """
    This class specifically creates the sql connections with the database
    """
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_ALX_DB")

    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
                user, password, host, port, database
            )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
