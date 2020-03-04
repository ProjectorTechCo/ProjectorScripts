from typing import List

from pandas import DataFrame

from config.common import DEFAULT_CONNECTION_STRING, TRANSFORMATIONS, PROCESS_TABLES_SCHEMA, TABLES_SCHEMA_TYPES
from db.postgres_connector import PostgresConnector
from excel_etl.executions.transformation.transformation import Transformation


def get_right_column_names(table_name):
    if table_name in PROCESS_TABLES_SCHEMA.keys():
        return PROCESS_TABLES_SCHEMA[table_name]
    elif table_name in TABLES_SCHEMA_TYPES.keys():
        return TABLES_SCHEMA_TYPES[table_name].keys()
    return None


class Execute(object):
    def __init__(self, table_name: str, column_schema: dict):
        self.table_name = table_name
        self.column_schema = column_schema
        self.db_conn = None

    def process(self, df: DataFrame):
        self.validate(df)

        # transform the data to output schema
        result = (TRANSFORMATIONS.get(self.table_name) or Transformation)(self.table_name,
                                                                          self.column_schema).transform(df)
        # TODO: Add a validation for every type of data(timestamp, string, integer)
        # TODO: add convertor to handle null values in columns
        #  (we don't want add_date to be null, it's just like insertion_time)
        for df in result:
            for table_name, df_dict in df.items():
                self.db_conn = PostgresConnector(DEFAULT_CONNECTION_STRING, table_name,
                                                 get_right_column_names(table_name))
                self.db_conn.insert(df_dict)
        return True

    def validate(self, df: DataFrame):
        difference_columns = set(self.column_schema.keys()).symmetric_difference(set(df.columns.values))
        if difference_columns:
            raise NotValidDataframe(
                "The schema is invalid, missing/redundant columns {columns}".format(columns=difference_columns))


class NotValidDataframe(Exception):
    pass
