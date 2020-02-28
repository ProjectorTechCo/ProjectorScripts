import logging


class Execute(object):
    def __init__(self, column_schema):
        self.column_schema = column_schema

    def process(self, df):
        self.validate(df)
        return []

    def validate(self, df):
        difference_columns = set(self.column_schema).symmetric_difference(set(df.columns.values))
        if difference_columns:
            raise NotValidDataframe(
                "The schema is invalid, missing/redundant columns {columns}".format(columns=difference_columns))


class NotValidDataframe(Exception):
    pass
