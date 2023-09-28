"""
Backend : db : session
========================
This module contains the sqlalchemy session management configuration.
"""

__author__ = "novasangeeth@outlook.com"

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#: Create the SQLA engine

engine = create_engine(
    url="",
    echo_pool=None
)
