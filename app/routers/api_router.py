from fastapi import APIRouter
from api.health_check import router as health_check_router

# from main import app


main_router = APIRouter()
# app.include_router(router=router)
main_router.include_router(router=health_check_router)
