#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity

storage_type = getenv("HBNB_TYPE_STORAGE")

# place_amenity = Table(
#     "place_amenity",
#     Base.metadata,
#     Column(
#         "place_id",
#         String(60),
#         ForeignKey("places.id"),
#         primary_key=True,
#         nullable=False,
#     ),
#     Column(
#         "amenity_id",
#         String(60),
#         ForeignKey("amenities.id"),
#         primary_key=True,
#         nullable=False,
#     ),
# )


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        cities = relationship("City", back_populates="places")
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        user = relationship("User", backref="places")
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        # amenities = relationship(
        #     "Amenity", secondary=place_amenity, viewonly=False)
        reviews = relationship(
            "Review", cascade="all, delete", back_populates="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
