from typing import List

from schemas.energy import ConsumptionResponse


class EnergyConsumption:

  @staticmethod
  def get_electricity_consumption() -> List[ConsumptionResponse]:
    consumption = [{
        'product': 'Electricity',
        'interval_start': 1671132600.0,
        'interval_end': 1671134400.0,
        'consumption': 0.1253,
    }]
    return consumption
