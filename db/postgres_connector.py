from typing import List

from sqlalchemy import create_engine, Table, MetaData, Column, String


class PostgresConnector(object):
    def __init__(self, connection_string: str, table_name: str = None, column_schema: List[str] = None):
        self.connection_string = connection_string
        self.table_name = table_name
        self.column_schema = column_schema
        self.db = create_engine(self.connection_string)
        self.table_metadata = self.__get_metadata()

    def __get_metadata(self):
        if not self.table_name:
            return None
        metadata = MetaData(self.db)
        return Table(self.table_name, metadata,
                     *[Column(column, String) for column in self.column_schema])

    def __get_type(self, value: object):
        print(value)
        if value == "nan":
            return None
        return value

    def insert(self, data: list):
        with self.db.connect() as conn:
            self.table_metadata.create(checkfirst=True)
            for row in data:
                row = {key: self.__get_type(value) for key, value in row.items()}
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