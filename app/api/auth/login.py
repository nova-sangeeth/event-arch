"""
Backend : api : authentication : login
=======================================
This module contains the endpoints for login
"""

from fastapi import APIRouter


__author__ = "novasangeeth@outlook.com"

# The login endpoint

router = APIRouter(prefix="/auth")


@router.post(path="/login", tags=["Auth"])
def api_login():
    """
    Endpoint to login to the system.
    """
    return "OK"
