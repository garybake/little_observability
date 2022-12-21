import os
from typing import Any, List

from fastapi import APIRouter

# from app import schemas
# from app.models import LocationKey

from schemas.energy import ConsumptionResponse
from models.energy import  EnergyConsumption

router = APIRouter()

@router.get("/electricity_consumption", response_model=List[ConsumptionResponse])
async def read_energy_consumption():
    resp = EnergyConsumption.get_electricity_consumption()

    return resp
