import os
from typing import Any

from fastapi import APIRouter

# from app import schemas
# from app.models import LocationKey

router = APIRouter()

@router.get("/electricity_consumption")
async def read_energy_consumption():
    return {"consumption": 10.1}
