"""
Backend : api : Health Check 
==============================
This module contains the endpoints for login
"""

from fastapi import APIRouter
from schema.health import HealthCheck

__author__ = "novasangeeth@outlook.com"

# Initialize the health check router
router = APIRouter()


@router.get(
    path="/health-check/",
    tags=["Health Check"],
    response_model=HealthCheck,
)
def api_health_check():
    """
    Endpoint to check the application's health
    """

    # TODO: Make changes to improve the endpoint to check the db connection.
    # TODO: Make changes to improve the endpoint to check the Redis Cache.
    return {"msg": "OK"}
