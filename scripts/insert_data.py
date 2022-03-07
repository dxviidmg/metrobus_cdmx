import csv
from metrobuses.models import Metrobus
from tqdm import tqdm


def insert():
    with open('data/prueba_fetchdata_metrobus.csv', newline='') as csvfile:
        reader = list(csv.DictReader(csvfile))
        for row in tqdm(reader):
            metrobus, metrobus_create = Metrobus.objects.get_or_create(number=row['vehicle_id'])
            metrobus.latitude = row['position_latitude']
            metrobus.longitude = row['position_longitude']
            metrobus.save()

def fix():
    metrobuses = Metrobus.objects.filter(townhall=None)
    
    for metrobus in tqdm(metrobuses):
#        print(metrobus)
        metrobus.update_townhall()
        metrobus.save()

def run():
    insert()
    fix()