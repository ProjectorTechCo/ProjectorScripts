from abc import ABC, abstractmethod


class Transformation(object):
    def __init__(self, sheet_name, column_schema):
        self.sheet_name = sheet_name
        self.column_schema = column_schema

    def transform(self, df):
        pass
