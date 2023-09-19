"""
Backend : api : Health Check 
==============================
This module contains the endpoints for login
"""

from fastapi import APIRouter

__author__ = "novasangeeth@outlook.com"

# Initialize the health check router
router = APIRouter()


@router.get("/health-check/", tags=["Health Check"])
def health_check() -> str:
    """
    An endpoint to check the application's health
    """
    # TODO: Make changes to improve the endpoint to check the db connection.
    # TODO: Make changes to improve the endpoint to check the Redis Cache.

    return {"msg": "OK"}
