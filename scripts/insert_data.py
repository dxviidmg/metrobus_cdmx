import csv
from metrobuses.models import Metrobus
from tqdm import tqdm


def insert():
    with open('data/prueba_fetchdata_metrobus.csv', newline='') as csvfile:
        reader = list(csv.DictReader(csvfile))
#        print(reader, len(reader))
        for row in tqdm(reader):
#        for row in pbar(reader):
#            print(row)
            metrobus, metrobus_create = Metrobus.objects.get_or_create(metrobus_id=row['vehicle_id'])
            metrobus.altitud = row['position_latitude']
            metrobus.longitud = row['position_longitude']
            metrobus.save()

def fix():
    metrobuses = Metrobus.objects.filter(alcaldia=None)
    
    for metrobus in tqdm(metrobuses):
        print(metrobus)
        metrobus.update_alcaldia()

def run():
#    insert()
    fix()