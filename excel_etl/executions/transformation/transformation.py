import locale
from datetime import datetime

from dateutil import parser

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def parse_json_type(value):
    # TODO: Add the json parsing part
    return value


def parse_bool_type(value):
    if value in ["כן"]:
        return True
    elif value in ["לא"]:
        return False
    return None


class Transformation(object):
    def __init__(self, sheet_name, column_schema):
        self.sheet_name = sheet_name
        self.column_schema = column_schema

    def transform(self, df):
        df_dict = df.to_dict('records')
        return [{self.sheet_name: self.change_df(df_dict)}]

    def change_df(self, df_dict):
        return [{key: self.handle_type(key, self.column_schema.get(key), value) for key, value in
                 df_dict_item.items()} for df_dict_item in df_dict]

    def handle_type(self, column_name, column_type, column_value):
        if column_type == str:
            return column_value
        elif column_type == int:
            return locale.atoi(str(column_value))
        elif column_type == dict:
            return parse_json_type(column_value)
        elif column_type == bool:
            return parse_bool_type(column_value)
        elif column_type == datetime:
            return column_value
            # return parser.parse(column_value)
        else:
            raise TypeNotFoundException(
                "The type {} for column {} with value {} in table {} was not found.".format(column_type, column_name,
                                                                                            column_value,
                                                                                            self.sheet_name))


class TypeNotFoundException(Exception):
    pass
