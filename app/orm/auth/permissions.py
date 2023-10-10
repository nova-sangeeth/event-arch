"""
Backend : orm : authentication : permissions
====================================
This module contains the SQLAlchemy models for user models
"""
__author__ = "novasangeeth@outlook.com"

# The user roles model
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from app.db.db import Base


class Permissions(Base):
    """
    The permission ORM model class
    """
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    permission = Column(String(length=128), nullable=True, unique=True)
