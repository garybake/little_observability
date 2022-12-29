from pydantic import BaseModel


class ConsumptionResponse(BaseModel):
    product: str
    interval_start: float
    interval_end: float
    consumption: float

class ConsumptionResponseReadable(ConsumptionResponse):
    # Human readable version of the response, dates formated as strings
    interval_start: str
    interval_end: str
