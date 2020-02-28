from abc import abstractmethod, ABC


class DBConnector(ABC):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    @abstractmethod
    def connect(self):
        raise NotImplementedError()

    @abstractmethod
    def select(self, query):
        raise NotImplementedError()

    @abstractmethod
    def insert(self, data):
        raise NotImplementedError()

    @abstractmethod
    def update(self, data):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, query):
        raise NotImplementedError()
