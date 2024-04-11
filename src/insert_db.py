def insert_localidad (instance=None, data=None):
    if not instance:
        return None
    if not data:
        return None
    
    query_insert_localidad = """
    INSERT INTO provincias (provincia, id, localidad, cp, id_prov_mstr)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    cursor = instance.cursor()
    cursor.executemany(query_insert_localidad, data)
    
    instance.commit()
    
    cursor.close()