import logging
import os

import pandas as pd

from config.common import TABLES_SCHEMA_TYPES, DEFAULT_CONNECTION_STRING
from config.queries import CREATE_QUERIES, DROP_QUERIES
from db.postgres_connector import PostgresConnector
from excel_etl.exceptions.io import *
from excel_etl.executions.execute import Execute

FILE_NAME = os.environ.get('MOCK_FILE')


def read_sheet(sheet_name, file_location=FILE_NAME):
    try:
        excel_file = pd.ExcelFile(file_location)
        if sheet_name not in excel_file.sheet_names:
            logging.error("sheet '{}' was not found".format(sheet_name))
            raise ExcelSheetNotFound(sheet_name)
        df = excel_file.parse(sheet_name)

        # Replace nulls with python None
        return df.where(pd.notnull(df), None)
    except FileNotFoundError:
        logging.error("the file '{}' was not found".format(file_location))
        raise ExcelFileNotFound(file_location)


def drop_and_create_tables():
    pg = PostgresConnector(connection_string=DEFAULT_CONNECTION_STRING)
    pg.create(DROP_QUERIES)
    pg.create(CREATE_QUERIES)


def main():
    drop_and_create_tables()
    for sheet_name, column_schema in TABLES_SCHEMA_TYPES.items():
        df = read_sheet(sheet_name)
        result = Execute(table_name=sheet_name, column_schema=column_schema).process(df)
        print(result)


if __name__ == '__main__':
    main()
