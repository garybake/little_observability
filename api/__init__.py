from fastapi import APIRouter

from api import energy

api_router = APIRouter()

api_router.include_router(
    energy.router, prefix="/energy", tags=["energy"]
)