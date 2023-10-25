"""
Backend : authentication : Roles
==================================
This module contains the SQLAlchemy models for user roles
"""
__author__ = "novasangeeth@outlook.com"

# The user roles model
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from app.db.db import Base


class Roles(Base):
    """
    The roles ORM model class
    """

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    role_name = Column(String(length=128), nullable=False, unique=True)
