from config.common import TABLES_SCHEMA_TYPES

DROP_QUERIES = "\n".join(
    list(reversed(["DROP TABLE IF EXISTS {table_name};".format(table_name=table_name) for table_name in TABLES_SCHEMA_TYPES.keys()])))
CREATE_QUERIES = """
        CREATE TABLE IF NOT EXISTS comp_projects (
            proj_id int4 NOT NULL,
            proj_status VARCHAR(100) NULL,
            proj_type VARCHAR (100) NULL,
            proj_pop_date timestamptz NULL,
            proj_description VARCHAR(1024) NULL,
            proj_area VARCHAR(100) NULL,
            proj_loc_data_pg VARCHAR(100) NULL,
            proj_loc_data_google json NULL,
            proj_address VARCHAR(100) NULL,
            proj_rating VARCHAR(100) NULL,
            proj_url VARCHAR(200) NULL,
            proj_extension_fields json NULL,
            proj_add_date timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
            proj_update_date timestamptz NULL,
            proj_entrepreneur_ids VARCHAR(100) NULL,
            proj_contractor_ids VARCHAR(100) NULL,
            proj_update_version int4 NULL,
            proj_contact_details json NULL,
            CONSTRAINT comp_projects_pk PRIMARY KEY (proj_id)
        ) WITH ( OIDS = FALSE );
        
        CREATE TABLE IF NOT EXISTS comp_buildings (
            build_id int4 NOT NULL,
            build_number varchar(100) NULL,
            build_proj_id int4 NOT NULL,
            build_status VARCHAR(100) NULL,
            build_floors VARCHAR(100) NULL,
            build_address VARCHAR(100) NOT NULL,
            build_description varchar(100) NULL,
            build_extension_fields json NULL,
            build_pop_date timestamptz DEFAULT CURRENT_TIMESTAMP,
            build_update_date timestamptz NULL,
            build_update_version int4 NULL,
            CONSTRAINT comp_buildings_pk PRIMARY KEY (build_id),
            CONSTRAINT comp_buildings_comp_projects_fk FOREIGN KEY (build_proj_id)
        REFERENCES comp_projects(proj_id) ON DELETE CASCADE 
        ) WITH ( OIDS = FALSE );
        
        CREATE TABLE IF NOT EXISTS comp_apps (
            app_id int4 NOT NULL,
            app_proj_id int4 NOT NULL, 
            app_build_id int4 NOT NULL,
            app_number VARCHAR(100) NULL,
            app_floor VARCHAR(100) NULL,
            app_type VARCHAR(100) NULL,
            app_porch VARCHAR(20) NOT NULL,
            app_porch_area VARCHAR(100) NULL,
            app_area VARCHAR(100) NULL,
            app_price VARCHAR(100) NULL,
            app_promotion VARCHAR(100) NULL,
            app_promotion_expire_date timestamptz,
            app_status VARCHAR(100) NULL,
            app_description VARCHAR(255) NULL,
            app_extension_fields json NULL,
            app_rooms VARCHAR(10) NULL,
            app_pop_date timestamptz,
            app_update_date timestamptz,
            app_parking VARCHAR(20) NULL,
            app_directions VARCHAR(20) NULL,
            app_update_version int4 DEFAULT 0,
            CONSTRAINT comp_apps_pk PRIMARY KEY (app_id),
            CONSTRAINT comp_apps_comp_projects_fk FOREIGN KEY (app_proj_id)
        REFERENCES comp_projects(proj_id) ON DELETE CASCADE
        ) WITH ( OIDS = FALSE );
        
        CREATE TABLE IF NOT EXISTS comp_users (
            user_id int4 NOT NULL,
            user_name VARCHAR(50) NULL,
            user_contact_details json NULL,
            user_email VARCHAR(255) NULL,
            user_password VARCHAR(50) NULL,
            user_add_date timestamptz DEFAULT CURRENT_TIMESTAMP,
            user_update_date timestamptz NULL,
            user_update_version int4 DEFAULT 0,
            user_extension_fields json NULL,
            user_role VARCHAR(50) NULL,
            CONSTRAINT comp_users_pk PRIMARY KEY (user_id)
        ) WITH ( OIDS = FALSE);
        
        CREATE TABLE IF NOT EXISTS comp_entrepreneurs (
            ent_id int4 NOT NULL,
            ent_description VARCHAR(1024) NOT NULL,
            ent_ratings float4 DEFAULT 0,
            ent_name VARCHAR(50) NULL,
            ent_web_site VARCHAR(255) NULL,
            ent_contact_details json NULL,
            ent_extension_fields json NULL,
            ent_update_version int4 DEFAULT 0,
            ent_add_date timestamptz DEFAULT CURRENT_TIMESTAMP,
            ent_update_date timestamptz,
            CONSTRAINT comp_entrepreneurs_pk PRIMARY KEY (ent_id)
        ) WITH ( OIDS = FALSE );
        
        CREATE TABLE IF NOT EXISTS comp_contractors (
            cont_id int4 NOT NULL,
            cont_type VARCHAR(50) NULL,
            cont_name VARCHAR(50) NULL,
            cont_web_site VARCHAR(255) NULL,
            cont_contact_details json NULL,
            cont_extension_fields json NULL,
            cont_ratings float4 DEFAULT 0,
            cont_update_version int4 DEFAULT 0,
            cont_add_date timestamptz DEFAULT CURRENT_TIMESTAMP,
            cont_update_date timestamptz
        );
        
        CREATE TABLE IF NOT EXISTS comp_resources (
            res_id int4 NOT NULL,
            res_class VARCHAR(10) NULL,
            res_file_url VARCHAR(255) NULL,
            res_object_type VARCHAR(10) NULL,
            res_type VARCHAR(50) NULL,
            res_dimensions VARCHAR(255) NULL,
            res_extension_fields json NULL,
            res_source_id VARCHAR(50) NULL,
            res_source_type VARCHAR(50) NULL,
            res_validate_date timestamptz,
            res_add_date timestamptz DEFAULT CURRENT_TIMESTAMP,
            res_update_date timestamptz,
            CONSTRAINT comp_resources_pk PRIMARY KEY (res_id)
        ) WITH ( OIDS = FALSE );
    """
