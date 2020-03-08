from pandas import DataFrame

from excel_etl.executions.transformation.transformation import Transformation

EXTRA_DETAILS_COLUMN = "res_extension_fields"
RESOURCE_ID = "res_id"
RESOURCE_SOURCE_TYPE = "res_source_type"
OUTPUT_TABLE_COLUMNS = ["res_id", "res_class", "res_type", "res_source_id", "res_source_type", "res_update_date"]

TABLES_COLUMNS = {
    "comp_2d_imgs": {
        "res_id": "img_id",
        "res_type": "img_type",
        "res_source_id": "img_source_id",
        "res_source_type": "img_source_type",
        "res_update_date": "img_update_date",
        "res_extension_fields": ["img_file_url", "img_dimensions", "img_class"],
    },
    "comp_3d_obj": {
        "res_id": "obj_id",
        "res_type": "obj_type",
        "res_source_id": "obj_source_id",
        "res_source_type": "obj_source_type",
        "res_update_date": "obj_update_date",
        "res_extension_fields": ["obj_validation_date", "obj_class"],
    },
    "comp_videos": {
        "res_id": "video_id",
        "res_type": "video_type",
        "res_source_id": "video_source_id",
        "res_source_type": "video_source_type",
        "res_update_date": "video_update_date",
        "res_extension_fields": ["videos_file_url", "video_size"],
    }
}


def create_json(df: DataFrame, keys: list):
    return [
        create_json_row(row, keys) for row in df.to_dict('records')
    ]


def create_json_row(df_dict: dict, keys: list):
    return {key: df_dict.get(key) for key in keys if df_dict.get(key)}


class ResourceTransformation(Transformation):
    def __init__(self, sheet_name, column_schema):
        super().__init__(sheet_name, column_schema)

    def transform(self, df: DataFrame):
        df = self.transform_schema(df)
        return super().transform(df)
        # TODO: Add the specific transformation for every resource.

    def transform_schema(self, df: DataFrame):
        # TODO: change the df according to the specific relevant schema
        for output_column, input_column in TABLES_COLUMNS.get(self.sheet_name).items():
            if output_column == EXTRA_DETAILS_COLUMN:
                df[output_column] = create_json(df, input_column)
            else:
                df[output_column] = df[input_column]
        # TODO: create an array for the RESOURCE_ID column to have a unique id
        df[RESOURCE_ID] = [f"{item[RESOURCE_ID]}_{item[RESOURCE_SOURCE_TYPE]}" for item in df.to_dict('records')]
        return df[TABLES_COLUMNS.get(self.sheet_name)]
