from io.db_connector import DBConnector


class PostgresConnector(DBConnector):
    def __init__(self, connection_string):
        super().__init__(connection_string)

    def connect(self):
        pass

    def select(self, query):
        pass

    def insert(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, query):
        pass
