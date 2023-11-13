"""
Backend : schema : Health Check
=================================
This module contains the pydantic models for health check.
"""

from pydantic import Field
from pydantic import BaseModel

__author__ = "novasangeeth@outlook.com"


class HealthCheck(BaseModel):
    """
    Schema for health check response.
    """

    #: The message field for the health check response.
    msg: str = Field(
        ...,
        alias="msg",
        description="The message field for health check status.",
    )
