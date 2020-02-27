import pandas as pd
from config import EXCEL_SHEETS_MAPPING


def read_sheet(sheet_name, file_location=""):
    return pd.read_excel(file_location, sheet_name=sheet_name)


def main():
    pass
    for sheet_name, class_execution in EXCEL_SHEETS_MAPPING.items():
        df = read_sheet(sheet_name)
        print(pd.io.sql.get_schema(df.reset_index(), sheet_name))
        result = class_execution.process(df)
    # find_location_from_text("הבימה")


if __name__ == '__main__':
    main()
