"""
Backend : api : authentication : Forgot Password
==================================================
This module contains the endpoints for forgot password
"""
from fastapi import APIRouter

__author__ = "novasangeeth@outlook.com"

router = APIRouter(prefix="/auth")
# The forgot password endpoint


@router.post(
    path="/forgot-password",
    tag=["Auth"],
)
def api_forgot_password():
    """
    Endpoint to forgot password.
    """
    return "OK"
