"""
Backend : orm : authentication : Users
========================================
This module contains the SQLAlchemy models for user authentication
"""
__author__ = "novasangeeth@outlook.com"

from app.db.db import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String


class User(Base):
    """
    The user ORM model class
    """

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, )
    username = Column(String(length=255), nullable=False, unique=True, )
    email = Column(String(length=255), nullable=True, unique=True, )
    first_name = Column(String(length=255), nullable=False, unique=False, )
    middle_name = Column(String(length=255), nullable=True, unique=False, )
    last_name = Column(String(length=255), nullable=True, unique=False, )
