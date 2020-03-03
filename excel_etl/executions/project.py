import itertools

from pandas import DataFrame
import numpy as np

from excel_etl.executions.transformation.transformation import Transformation

RELATION_DF_COLUMNS = {"proj_entrepreneur_ids": "ent", "proj_contractor_ids": "cont"}


class ProjectTransformation(Transformation):
    def __init__(self, sheet_name, column_schema):
        Transformation.__init__(self, sheet_name, column_schema)

    def transform(self, df: DataFrame):
        return list(itertools.chain(*[DataFrame(np.array([item.values() for item in data]), columns=data[0].keys())
                                      for data in self.split_dataframes(df)]))

    def split_dataframes(self, df: DataFrame):
        return [Transformation.transform(self, df[list(set(df.columns.values.tolist()) - set(RELATION_DF_COLUMNS))]),
                self.get_project_relation_table(df)]

    def get_project_relation_table(self, df):
        prepared_data_for_explode = []
        for row_num, row in df.iterrows():
            for column, column_type in RELATION_DF_COLUMNS.items():
                prepared_data_for_explode.append([
                    self.generate_item_type(column_type, row["proj_id"], item) for item in row[column].split(',')
                ])
        return list(itertools.chain(*prepared_data_for_explode))

    def generate_item_type(self, column_type, proj_id, column_value):
        return {
            "type": column_type,
            "proj_id": proj_id,
            "worker_id": column_value
        }
