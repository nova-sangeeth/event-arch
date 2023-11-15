"""
Backend : Schema : Auth : Login
=================================
This module contains the schema for login.
"""
from pydantic import BaseModel
from pydantic import Field

__author__ = "novasangeeth@outlook.com"


class Login:
    """
    Schema for login.
    """

    username: str = Field(
        ...,
        alias="login",
        description="The username for login",
    )

    password: str = Field(
        ...,
        alias="password",
        description="The password for login",
    )
