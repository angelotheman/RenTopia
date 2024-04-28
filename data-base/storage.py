#!/usr/bin/python3
"""Contains the DataBase storage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from app.models.amenity import Amenity
from app.models.apartment import Apartment
from app.models.base_model import Basemodel
from app.models.booking import Booking
from app.models.location import Location
from app.models.review import Review
from app.models.user import User
from app.models.base_model import Base
import os

classes = {
    'amenity': Amenity,
    'apartment': Apartment,
    'basemodel': Basemodel,
    'booking': Booking,
    'location': Location,
    'review': Review,
    'user': User
}

class Storage:
    """Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialzes the database"""
        username = 'USERNAME'
        database = 'DATABASE'
        host = 'HOST'
        passwd = 'PASSWORD'

        self.__engine = create_engine('mysql+mysqldb//{}:{}@{}/{}'.
                                      format(os.getenv(username),
                                             os.getenv(passwd),
                                             os.getenv(host),
                                             os.getenv(database)))

        Base.metadata.create_all(self.__engine)
        Session =  sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session

    def all(self, cls=None):
        """Queries for all instances of the classes
        Stores the result in dictionary with classname_id as key

        Return: 
            Dict
        """
        result = {}
        if cls is not None:
            for item in classes.values():
                if item is classes[cls] or item is cls:
                    ob = self.__session.query(item).all()
                    for obj in ob:
                        key = obj.__class__.__name__ + '_' + obj.id
                        result[key] = obj
        else:
            ob = self.__session.query().all()
            for obj in ob:
                key = obj.__class__.__name__ + '_' + obj.id
                result[key] == obj

        return result

    def get(self, cls, id):
        if cls is not None and id is not None:
            if cls in classes.values():
                ob = self.__session.query(cls)
                return ob.get(id)
        return None


    def new(self, cls):
        """Adds a new instance of the model to the database session"""
        if cls is not None:
            self.__session.add(cls)
    
    def save(self):
        """saves the newly added model to the session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Deletes an object in the database session"""
        if obj is not None:
            self.__session.delete(obj)
