#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """Review class"""

    __tablename__ = "reviews"

    if storage_type == "db":
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(Text(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
