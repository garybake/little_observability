from typing import List

from core.db import DBConnection
from schemas.energy import ConsumptionResponse


class EnergyConsumption:

    @staticmethod
    def get_electricity_consumption(count: int = 100) -> List[ConsumptionResponse]:
        if not count:
            count = 100
        db = DBConnection()
        results = db.execute(sql_string='SELECT * FROM CONSUMPTION LIMIT ?;', params=[str(count)])
        column_names = ['product', 'interval_start', 'interval_end', 'consumption']
        consumption = [dict(zip(column_names, row)) for row in results]

        return consumption

    @staticmethod
    def get_electricity_consumption_latest() -> List[ConsumptionResponse]:
        db = DBConnection()
        results = db.execute(sql_string='SELECT * FROM CONSUMPTION ORDER BY INTERVAL_START DESC LIMIT 1;')
        column_names = ['product', 'interval_start', 'interval_end', 'consumption']
        consumption = [dict(zip(column_names, row)) for row in results]

        return consumption


    @staticmethod
    def row_db_format(row):
        return [row.interval_start, row.interval_end, row.consumption]

    @classmethod
    def save_to_db(cls, rows):
        all_rows = [cls.row_db_format(r) for r in rows]

        sql_string = 'REPLACE INTO CONSUMPTION (PRODUCT, INTERVAL_START, INTERVAL_END, CONSUMPTION) VALUES("Electricity", ?,?,?)'

        db = DBConnection()
        results = db.save_to_db(sql_string=sql_string, data=all_rows)
        return results

    @classmethod
    def add_electricity_consumption(cls, data: List[ConsumptionResponse]) -> int:
        update_count = cls.save_to_db(data)
        return update_count
