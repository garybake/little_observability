from pydantic import BaseModel


class ConsumptionResponse(BaseModel):
    product: str
    interval_start: float
    interval_end: float
    consumption: float
