"""
Backend : routers : API routers
=================================
This module contains the API routers for the backend application
"""
__author__ = "novasangeeth@outlook.com"

from fastapi import APIRouter

# from ..api.health_check import router as health_check_router
from api import router as health_check_router
from api.auth.login import router as login_router
from api.auth.logout import router as logout_router
from api.auth.forgot_pasword import router as forgot_pwd_router
from api.auth.reset_password import router as reset_pwd_router


# Instantiate a main router for the application
main_router = APIRouter()

#: The health check router.
main_router.include_router(router=health_check_router)

#: The login router.
main_router.include_router(router=login_router)

#: The logout router.
main_router.include_router(router=logout_router)

#: The forgot_password router.
main_router.include_router(router=forgot_pwd_router)

#: The reset_password router.
main_router.include_router(router=reset_pwd_router)
