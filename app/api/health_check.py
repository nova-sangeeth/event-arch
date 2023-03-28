from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check/", tags=["Health Check"])
async def read_users():
    return {"data": "OK"}
