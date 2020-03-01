from abc import ABC, abstractmethod
import locale
from dateutil import parser
from datetime import datetime

from config.common import TABLES_SCHEMA_TYPES

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

    def transform(self, df_dict):
        return [{key: self.handle_type(key, TABLES_SCHEMA_TYPES.get(self.sheet_name).get(key), value) for key, value in
                 df_dict.items()}]

    def handle_type(self, column_name, column_type, column_value):
        if type(column_type) == str:
            return column_type
        elif type(column_type) == int:
            return locale.atoi(column_value)
        elif type(column_type) == dict:
            return parse_json_type(column_value)
        elif type(column_type) == bool:
            return parse_bool_type(column_value)
        elif type(column_type) == datetime:
            return parser.parse(column_value)
        else:
            raise TypeNotFoundException(
                "The type {} for column {} with value {} in table {} was not found.".format(column_type, column_name,
                                                                                            column_value,
                                                                                            self.sheet_name))


class TypeNotFoundException(Exception):
    pass
