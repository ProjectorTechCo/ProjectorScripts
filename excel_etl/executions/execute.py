from abc import ABC, abstractmethod
import logging


class IExecute(ABC):
    def __init__(self, prefix, column_schema):
        self.prefix = prefix
        self.column_schema = column_schema

    @abstractmethod
    def process(self, df):
        raise NotImplementedError()

    @staticmethod
    def log_action(message):
        logging.info(message)
