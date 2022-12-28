from typing import List, Union

from fastapi import APIRouter

from schemas.energy import ConsumptionResponse
from models.energy import EnergyConsumption


router = APIRouter()


@router.get("/electricity_consumption", response_model=List[ConsumptionResponse])
async def read_energy_consumption(count: Union[int, None] = None) -> ConsumptionResponse:
    resp = EnergyConsumption.get_electricity_consumption(count=count)
    print(f"count: {count}")
    return resp


@router.post("/electricity_consumption")
async def post_energy_consumption(cons: List[ConsumptionResponse]):
    added = EnergyConsumption().add_electricity_consumption(data=cons)
    resp = {'status': 'success', 'rows_changed': added}
    return resp
