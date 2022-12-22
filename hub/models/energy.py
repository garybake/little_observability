from typing import List

from core.db import DB
from schemas.energy import ConsumptionResponse


class EnergyConsumption:

  @staticmethod
  def get_electricity_consumption(count: int = 100) -> List[ConsumptionResponse]:
    if not count:
      count = 100
    d = DB()
    results = d.execute(sql_string='SELECT * FROM CONSUMPTION LIMIT ?;', params=[str(count)], as_dict=False)
    column_names = ['product', 'interval_start', 'interval_end', 'consumption']
    consumption = [dict(zip(column_names, row))  
              for row in results]

    return consumption
