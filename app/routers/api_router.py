"""
Backend : routers : API routers
=================================
This module contains the API routers for the backend application
"""
__author__ = "novasangeeth@outlook.com"

from fastapi import APIRouter
from app.api.health_check import router as health_check_router

# Instantiate a main router for the application
main_router = APIRouter()

# Add the health checkouter to the main router
main_router.include_router(router=health_check_router)
