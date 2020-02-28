import logging
import os

import pandas as pd

from config.common import TABLES_SCHEMA
from excel_etl.exceptions.io import *
from excel_etl.executions.execute import Execute

FILE_NAME = os.environ.get('MOCK_FILE')


def read_sheet(sheet_name, file_location=FILE_NAME):
    try:
        excel_file = pd.ExcelFile(file_location)
        if sheet_name not in excel_file.sheet_names:
            logging.error("sheet '{}' was not found".format(sheet_name))
            raise ExcelSheetNotFound(sheet_name)
        return excel_file.parse(sheet_name)
    except FileNotFoundError:
        logging.error("the file '{}' was not found".format(file_location))
        raise ExcelFileNotFound(file_location)


def get_parameters():


def main():
    for sheet_name, table_schema in TABLES_SCHEMA.items():
        df = read_sheet(sheet_name)
        result = Execute(column_schema=table_schema).process(df)
        print(result)


if __name__ == '__main__':
    main()
