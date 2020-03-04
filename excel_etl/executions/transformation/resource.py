from excel_etl.executions.transformation.transformation import Transformation


class ResourceTransformation(Transformation):
    def __init__(self, sheet_name, column_schema):
        super().__init__(sheet_name, column_schema)

    def transform(self, df_dict):
        return self.transform(df_dict)
        # TODO: Add the specific transformation for every resource.

    def get_new_schema(self, transformed_data):
        # TODO: Use the prefix to determine what object it is.
        return {
            "res_id": transformed_data.get('')
        }
