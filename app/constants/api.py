"""
Backend : Constants : Api
==========================
This module contains the constants for API endpoints and routers.
"""
from enum import Enum


__author__ = "novasangeeth@outlook.com"

API_PREFIX = "/api"


class ApiTagEnum(Enum, str):
    """
    The api endpoint tags
    """

    #:
    AUTHENTICATION = "AUTH"
    HEALTH_CHECK = "HEALTH-CHECK"
