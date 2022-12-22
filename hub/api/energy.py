import os
from typing import Any, List, Union

from fastapi import APIRouter

from schemas.energy import ConsumptionResponse
from models.energy import EnergyConsumption


router = APIRouter()

@router.get("/electricity_consumption", response_model=List[ConsumptionResponse])
async def read_energy_consumption(count: Union[int, None] = None) -> ConsumptionResponse:
    resp = EnergyConsumption.get_electricity_consumption(count=count)
    print(f"count: {count}")

    return resp
