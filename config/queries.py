QUERIES = {
    "comp_projects": """
        DROP TABLE IF EXISTS comp_projects;
        CREATE TABLE IF NOT EXISTS comp_projects (
            proj_id int4 NOT NULL,
            proj_status VARCHAR(100) NULL,
            proj_type VARCHAR (100) NULL,
            proj_pop_date timestamptz NULL,
            proj_description VARCHAR(1024) NULL,
            proj_area VARCHAR(100) NULL,
            proj_loc_data_pg VARCHAR(100) NULL,
            proj_loc_data_google VARCHAR(100) NULL,
            proj_address VARCHAR(100) NULL,
            proj_rating VARCHAR(100) NULL,
            proj_url VARCHAR(200) NULL,
            proj_extension_fields json NULL,
            proj_add_date timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
            proj_update_date timestamptz NULL,
            proj_entrepreneur_ids VARCHAR(100) NULL,
            proj_contractor_ids VARCHAR(100) NULL,
            proj_update_version int4 NULL,
            proj_contact_details VARCHAR(200) NULL,
            CONSTRAINT comp_projects_pk PRIMARY KEY (proj_id)
        ) WITH ( OIDS = FALSE );
    """,
    "comp_buildings": """
        CREATE TABLE IF NOT EXISTS comp_buildings (
            build_id int4 NOT NULL,
            build_number varchar(100) NULL,
            build_proj_id int4 NOT NULL,
            build_status VARCHAR(100) NULL,
            build_floors VARCHAR(100) NULL,
            build_address VARCHAR(100) NOT NULL,
            build_description varchar(100) NULL,
            build_extenstion_fields json NULL,
            build_pop_date timestamptz DEFAULT CURRENT_TIMESTAMP,
            build_update_date timestamptz NULL,
            build_update_version int4 NULL,
            CONSTRAINT comp_buildings_pk PRIMARY KEY (build_id),
            CONSTRAINT comp_buildings_comp_projects_fk FOREIGN KEY (build_proj_id)
        REFERENCES comp_projects(proj_id) ON DELETE CASCADE 
        ) WITH ( OIDS = FALSE );
    """
}
