import itertools

from pandas import DataFrame

from excel_etl.executions.transformation.transformation import Transformation
from excel_etl.external_api.google_api import find_bulk_locations

RELATION_DF_COLUMNS = {"proj_entrepreneur_ids": "ent", "proj_contractor_ids": "cont"}


class ProjectTransformation(Transformation):
    def __init__(self, sheet_name, column_schema):
        Transformation.__init__(self, sheet_name, column_schema)

    def transform(self, df: DataFrame):
        df = self.enrich_with_google_coordinates(df)
        return self.split_dataframes(df)

    def split_dataframes(self, df: DataFrame):
        return [Transformation.transform(self, df[list(set(df.columns.values.tolist()) - set(RELATION_DF_COLUMNS))])[0],
                {"comp_proj_workers_relations": self.get_project_relation_table(df)}]

    def enrich_with_google_coordinates(self, df: DataFrame):
        df["proj_loc_data_google"] = find_bulk_locations(df["proj_address"])
        return df

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
