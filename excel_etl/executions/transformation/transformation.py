import json
import locale
from datetime import datetime
from typing import Dict, List

from pandas import DataFrame

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

hebrew_to_english_keys = {
    "אימייל": "email",
    "דוא\"ל": "email",
    "טלפון": "phone"
}


def get_right_translation(item):
    return hebrew_to_english_keys.get(item) or item


def parse_json_type(value):
    # TODO: Add the json parsing part
    if type(value) == dict:
        return json.dumps(value)
    return json.dumps(
        {} if not value else {get_right_translation(item.split(":")[0]): item.split(":")[1].strip() for item in
                              list(filter(lambda field: ':' in field, [v for v in value.split("\n")]))})


def parse_bool_type(value):
    if value in ["כן"]:
        return True
    elif value in ["לא"]:
        return False
    return None


def remove_insertion_time(df: DataFrame):
    return df.drop(columns=[c for c in df.columns.values.tolist() if "_add_date" in c])


class Transformation(object):
    def __init__(self, sheet_name: str, column_schema: Dict):
        self.sheet_name = sheet_name
        self.column_schema = column_schema

    def transform(self, df: DataFrame):
        df = remove_insertion_time(df)
        df_dict = df.to_dict('records')
        return [{self.sheet_name: self.change_df(df_dict)}]

    def change_df(self, df_dict: List[Dict]):
        return [{key: self.handle_type(key, self.column_schema.get(key), value) for key, value in
                 df_dict_item.items()} for df_dict_item in df_dict]

    def handle_type(self, column_name: str, column_type: str, column_value: str):
        if column_type == str:
            return column_value
        elif column_type == int:
            return locale.atoi(str(column_value))
        elif column_type == dict:
            return parse_json_type(column_value)
        elif column_type == bool:
            return parse_bool_type(column_value)
        elif column_type == datetime:
            # TODO: handle date parsing
            return column_value
            # return parser.parse(column_value)
        else:
            raise TypeNotFoundException(
                "The type {} for column {} with value {} in table {} was not found.".format(column_type, column_name,
                                                                                            column_value,
                                                                                            self.sheet_name))


class TypeNotFoundException(Exception):
    pass
