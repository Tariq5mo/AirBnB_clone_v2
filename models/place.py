#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review as re
from sqlalchemy import Integer, Float, String, Column, ForeignKey
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import relationship
from os import getenv


metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             nullable=False, primary_key=True
                             ),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False, primary_key=True
                             )
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(re, backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary="place_amenity",
                                 viewonly=False, overlaps="place_amenities")
    else:
        @property
        def reviews(self):
            from models import storage

            li = []
            di = storage.all()
            for key in di:
                if str(key).split(".")[0] == "Review":
                    obj = di[key]
                    if obj.place_id == self.id:
                        li.append(obj)
            return li

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity

            li = []
            di = storage.all(Amenity)
            for amenity in di:
                if di[amenity].id in self.amenity_ids:
                    li.append(di[amenity])
            return li

        @amenities.setter
        def amenities(self, amenity_obj):
            """
            Handles 'append' method for adding an 'Amenity.id'
            to the attribute 'amenity_ids'.
            This method should accept only 'Amenity' object,
            otherwise, do nothing.

            Args:
                amenity_id (str): _description_
            """
            from models.amenity import Amenity
            if isinstance(amenity_obj, Amenity):
                """ if amenity_obj.id not in self.amenity_ids: """
                self.amenity_ids.append(amenity_obj.id)
