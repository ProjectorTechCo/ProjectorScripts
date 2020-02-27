from excel_etl.executions.project import Project

EXCEL_SHEETS = ['projects', 'buildings', 'apps', 'users', 'entrepreneurs', 'contractors', '2d_imgs', '3d_obj',
                'comp_videos']

EXCEL_SHEETS_MAPPING = {
    "comp_projects": Project(prefix='proj', column_schema={})
}