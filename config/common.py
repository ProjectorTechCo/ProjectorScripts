from datetime import datetime

TABLES_SCHEMA = {
    'comp_projects': ['proj_id', 'proj_status', 'proj_type', 'proj_pop_date', 'proj_description', 'proj_area',
                      'proj_loc_data_pg', 'proj_loc_data_google', 'proj_address', 'proj_rating', 'proj_url',
                      'proj_extension_fields', 'proj_add_date', 'proj_update_date', 'proj_entrepreneur_ids',
                      'proj_contractor_ids', 'proj_update_version', 'proj_contact_details'],
    'comp_buildings': ['build_id', 'build_number', 'build_proj_id', 'build_status', 'build_floors', 'build_address',
                       'build_description', 'build_extension_fields', 'build_pop_date', 'build_update_date',
                       'build_update_version'],
    'comp_apps': ['app_id', 'app_build_id', 'app_number', 'app_floor', 'app_type', 'app_proj_id', 'app_porch',
                  'app_porch_area', 'app_area', 'app_price', 'app_promotion', 'app_promotion_expire_date', 'app_status',
                  'app_description', 'app_extension_fields', 'app_rooms', 'app_pop_date', 'app_update_date',
                  'app_parking', 'app_directions', 'app_update_version'],
    'comp_users': ['user_id', 'user_name', 'user_contact_details', 'user_email', 'user_password', 'user_add_date',
                   'user_update_date', 'user_update_version', 'user_extension_fields', 'user_role'],
    'comp_entrepreneurs': ['ent_id', 'ent_description', 'ent_ratings', 'ent_name', 'ent_web_site',
                           'ent_contact_details', 'ent_extension_fields', 'ent_update_version', 'ent_add_date',
                           'ent_update_date'],
    'comp_contractors': ['cont_id', 'cont_name', 'cont_web_site', 'cont_contact_details', 'cont_type',
                         'cont_extension_fields', 'cont_ratings', 'cont_update_version', 'cont_add_date',
                         'cont_update_date'],
    'comp_2d_imgs': ['img_id', 'img_class', 'img_file_url', 'img_type', 'img_dimensions', 'img_extension_fields',
                     'img_source_id', 'img_source_type', 'img_add_date', 'img_update_date'],
    'comp_3d_obj': ['obj_id', 'obj_class', 'obj_file_url', 'obj_type', 'obj_extension_fields', 'obj_add_date',
                    'obj_validate_date', 'obj_source_id', 'obj_source_type'],
    'comp_videos': ['video_id', 'video_size', 'video_type', 'videos_source_id', 'videos_source_type', 'video_add_date',
                    'video_update_date', 'videos_file_url', 'video_extension_fields']
}

DEFAULT_CONNECTION_STRING = "postgres://postgres:postgres@localhost:5432/postgres"

TABLES_SCHEMA_TYPES = {
    'comp_projects': {'proj_id': int,
                      'proj_status': str,
                      'proj_type': str,
                      'proj_pop_date': datetime,
                      'proj_description': str,
                      'proj_area': str,
                      'proj_loc_data_pg': str,
                      'proj_loc_data_google': str,
                      'proj_address': str,
                      'proj_rating': str,
                      'proj_url': str,
                      'proj_extension_fields': dict,
                      'proj_add_date': datetime,
                      'proj_update_date': datetime,
                      'proj_entrepreneur_ids': str,
                      'proj_contractor_ids': str,
                      'proj_update_version': str,
                      'proj_contact_details': str
                      }
}
