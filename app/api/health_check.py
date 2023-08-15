from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check/", tags=["Health Check"])
async def read_users():
    # TODO: Make changes to improve the endpoint to check the db connection.
    # TODO: Make changes to improve the endpoint to check the Redis Cache.

    return {"reponse": "OK"}
