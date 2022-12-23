import os
import sqlite3


class DB:
    def __init__(self):
        self.db_path = os.getenv('DB_PATH')

    def get_conn(self):
        conn = sqlite3.connect(self.db_path)
        return conn

    def execute(self, sql_string: str, params=[], as_dict=True):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql_string, params)

        results = cursor.fetchall()

        if as_dict:
            desc = cursor.description
            column_names = [col[0] for col in desc]
            results = [dict(zip(column_names, row)) for row in results]

        cursor.close()

        return results
