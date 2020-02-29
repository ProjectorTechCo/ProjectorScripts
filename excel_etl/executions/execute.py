from typing import List

from pandas import DataFrame

from config.common import DEFAULT_CONNECTION_STRING
from db.postgres_connector import PostgresConnector


class Execute(object):
    def __init__(self, table_name: str, column_schema: List[str]):
        self.table_name = table_name
        self.column_schema = column_schema
        self.db_conn = PostgresConnector(DEFAULT_CONNECTION_STRING, table_name,
                                         column_schema)

    def process(self, df: DataFrame):
        self.validate(df)
        # TODO: Add a validation for every type of data(timestamp, string, integer)
        # TODO: add convertor to handle null values in columns
        #  (we don't want add_date to be null, it's just like insertion_time)
        self.db_conn.insert(df[self.column_schema].to_dict('records'))
        return self.column_schema

    def validate(self, df: DataFrame):
        difference_columns = set(self.column_schema).symmetric_difference(set(df.columns.values))
        if difference_columns:
            raise NotValidDataframe(
                "The schema is invalid, missing/redundant columns {columns}".format(columns=difference_columns))


class NotValidDataframe(Exception):
    pass
