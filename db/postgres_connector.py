from typing import List

from sqlalchemy import create_engine, Table, MetaData, Column, String


class PostgresConnector(object):
    def __init__(self, connection_string: str, table_name: str = None, column_names: list = None):
        self.connection_string = connection_string
        self.table_name = table_name
        self.column_names = column_names
        self.db = create_engine(self.connection_string)
        self.table_metadata = self.__get_metadata()

    def __get_metadata(self):
        if not self.table_name:
            return None
        metadata = MetaData(self.db)
        return Table(self.table_name, metadata,
                     *[Column(column, String) for column in self.column_names])

    def insert(self, data: list):
        with self.db.connect() as conn:
            self.table_metadata.create(checkfirst=True)
            for row in data:
                statement = self.table_metadata.insert().values(**row)
                conn.execute(statement)

    def drop(self):
        self.table_metadata.drop(checkfirst=True)

    def create(self, query=None):
        if query is not None:
            self.__action(query)
        else:
            self.table_metadata.create(checkfirst=True)

    def count(self):
        return self.__query(self.table_metadata.count())[0][0]

    def select(self, query):
        return self.__query(query)

    def __query(self, query_callback):
        with self.db.connect() as conn:
            return [row for row in conn.execute(query_callback)]

    def __action(self, query):
        with self.db.connect() as conn:
            conn.execute(query)
