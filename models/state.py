#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(City, backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """
            getter attribute 'cities' that returns the list of 'City' instances
            with 'state_id' equals to the current 'State.id'.
            """
            import models
            from models.city import City
            cities_list = []
            for key in models.storage.all(City).values():
                if key.state_id == self.id:
                    cities_list.append(key)
            return cities_list
