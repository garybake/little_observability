from typing import List, Union

from fastapi import APIRouter

from schemas.energy import ConsumptionResponse, ConsumptionResponseReadable
from models.energy import EnergyConsumption
from core.utils import unix_to_datetime_string


router = APIRouter()


@router.get("/electricity_consumption", response_model=List[ConsumptionResponse])
async def read_energy_consumption(count: Union[int, None] = None) -> ConsumptionResponse:
    resp = EnergyConsumption.get_electricity_consumption(count=count)
    return resp


@router.get("/electricity_consumption/latest", response_model=ConsumptionResponseReadable)
async def read_energy_consumption_latest() -> ConsumptionResponseReadable:
    resp = EnergyConsumption.get_electricity_consumption_latest()[0]
    resp['interval_start'] = unix_to_datetime_string(resp['interval_start'])
    resp['interval_end'] = unix_to_datetime_string(resp['interval_end'])
        
    return resp


@router.post("/electricity_consumption")
async def post_energy_consumption(cons: List[ConsumptionResponse]):
    added = EnergyConsumption().add_electricity_consumption(data=cons)
    resp = {'status': 'success', 'rows_changed': added}
    return resp
