def select_from_provincia (conn, provincia):
    query = """
    SELECT localidad, id, cp, id_prov_mstr FROM provincias WHERE provincia = %s
    """
    
    cursor = conn.cursor()
    cursor.execute(query, (provincia,))
    
    result = cursor.fetchall()
    
    cursor.close()
    
    return result



def get_provincias (conn):
    query = """
    SELECT DISTINCT provincia FROM provincias
    """
    
    provincias = []
    
    cursor = conn.cursor()
    cursor.execute(query)
    
    result = cursor.fetchall()
    
    for row in result:
        provincias.append(row[0])
    
    cursor.close()
    
    return provincias