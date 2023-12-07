"""
Backend : api : authentication : Reset Password
=======================================
This module contains the endpoints for reset password
"""
from fastapi import APIRouter

__author__ = "novasangeeth@outlook.com"

router = APIRouter(prefix="/auth")
# The reset password endpoint


@router.post(
    path="/reset-password",
    tags=["Auth"],
)
def api_reset_password():
    """
    Endpoint to reset password.
    """
    return "OK"
