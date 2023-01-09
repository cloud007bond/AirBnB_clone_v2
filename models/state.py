#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """Representation of State class
    args:
        __tablename___(str): Name of the table
        id (Integer): unique identifier of table's row
        name (String): name of states
        cities (Integer): State-City relationship
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states',
                          cascade='all, delete, delete-orphan')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Get a list of all related City objects"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
