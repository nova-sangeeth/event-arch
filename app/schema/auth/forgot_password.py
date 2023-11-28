"""
Backend : Schema : Auth : Forgot Password
===========================================
This module contains the schema for forgot password.
"""
from pydantic import BaseModel
from pydantic import Field


__author__ = "novasangeeth@outlook.com"


class ForgotPassword(BaseModel):
    """
    Schema for forgot password.
    """

    token: str = Field(
        ...,
        alias="token",
        description="The password reset token.",
    )
