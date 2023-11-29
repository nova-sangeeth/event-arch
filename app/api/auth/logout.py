"""
Backend : api : authentication : Logout
=======================================
This module contains the endpoints for logout
"""
from fastapi import APIRouter

__author__ = "novasangeeth@outlook.com"


router = APIRouter(prefix="/auth")
# The logout endpoint


@router.post(
    path="/logout",
    tags=["Auth"],
)
def api_logout():
    """
    Endpoint to logout to the system.
    """
    return "OK"
