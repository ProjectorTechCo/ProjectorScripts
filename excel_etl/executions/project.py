from excel_etl.executions import IExecute


class Project(IExecute):
    def __init__(self, prefix, column_schema):
        super().__init__(prefix, column_schema)

    def process(self, df):
        print(df)
        return df
