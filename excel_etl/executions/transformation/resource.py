from pandas import DataFrame

from excel_etl.executions.transformation.transformation import Transformation

columns = {
    ""
}

class ResourceTransformation(Transformation):
    def __init__(self, sheet_name, column_schema):
        super().__init__(sheet_name, column_schema)

    def transform(self, df_dict):
        return super().transform(df_dict)
        # TODO: Add the specific transformation for every resource.

    def exchange_df(self, df: DataFrame):
        # TODO: change the df according to the specific relevant schema
        pass

    def get_new_schema(self, transformed_data):
        # TODO: Use the prefix to determine what object it is.
        return {
            "res_id": transformed_data.get('')
        }
