import csv
import pathlib

from src.connections import db_connection
from src.create_table import create_table
from src.read_localidades import get_localidades
from src.insert_db import insert_localidad
from src.read_db import get_provincias, select_from_provincia


file_csv = "localidades.csv"

def format_file_csv_name (provincia):
    provincia = provincia.lower().replace(" ", "-")
    return f"{provincia}.csv"

def write_csv_file (file_name, data):
    pathlib.Path(__file__).parent.joinpath("data", "localidades").mkdir(parents=True, exist_ok=True)
    path = pathlib.Path(__file__).parent.joinpath("data", "localidades", file_name)
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return path

def main ():
    # se crea la conexion a la base de datos
    conn = db_connection()
    
    # se crea la tabla para almacenar los datos
    create_table(conn)
    
    # se obtiene el path del archivo csv
    path = pathlib.Path(__file__).parent.joinpath("data", file_csv)
    
    # se obtienen las localidades del archivo csv
    rows = get_localidades(path)
    
    # se preparan los datos para insertar en la base de datos
    values = []
    for row in rows:
        if row[3] == "":
            row[3] = 0
        one_row = (str(row[0]), int(row[1]), str(row[2]), int(row[3]), int(row[4]))
        values.append(one_row)
    
    # se insertan los datos en la base de datos
    insert_localidad(conn, values)
    
    # se pide una list de las provincias
    provincias = get_provincias(conn)
    
    # se pide todas las localidades por provinias
    for provincia in provincias:
        file_name = format_file_csv_name(provincia)
        result = select_from_provincia(conn, provincia)
        
        # se crea y escribe el archivo csv
        write_csv_file(file_name, result)
    
    
    # se cierra la conexion a la base de datos
    conn.close()
    
if __name__ == "__main__":
    main()
    
    
# ["id","localidad","cp","id_prov_mstr"]
