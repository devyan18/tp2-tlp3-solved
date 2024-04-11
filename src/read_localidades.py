import csv
from pathlib import Path

def get_localidades (path):
    localidades = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            localidades.append(row)
    return localidades