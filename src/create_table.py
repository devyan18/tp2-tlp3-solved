def create_table (instance=None):
    if not instance:
        return None
    
    drop_table = """
    DROP TABLE IF EXISTS provincias
    """
    
    query_create_table = """
    CREATE TABLE IF NOT EXISTS provincias (
        id_provincia INT PRIMARY KEY AUTO_INCREMENT,
        provincia VARCHAR(255),
        id INTEGER,
        localidad VARCHAR(255),
        cp INTEGER,
        id_prov_mstr INTEGER
    )
    """
    # cursor:
    
    cursor = instance.cursor()
    
    cursor.execute(drop_table)
    cursor.execute(query_create_table)
    
    instance.commit()
    
    cursor.close()