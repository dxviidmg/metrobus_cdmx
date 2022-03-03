from django.db import models
from alcaldias.models import Estado, Alcaldia
from geopy.geocoders import Nominatim
from time import sleep


class Geolocalizacion(models.Model):
    altitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)

    class Meta:
        abstract = True

    def covert_to_point(self):
        return str(self.altitud) + ', ' + str(self.longitud)

    def get_localizacion(self):
        geographic_point = self.covert_to_point()
        geolocator = Nominatim(user_agent="http")
        try:
            location = geolocator.reverse(geographic_point, timeout=10)
        except Exception as e:
            location = None
            print('error', e)
#            input()
        
        return location

    def convert_location_on_list(self):
        location = self.get_localizacion()
        if location == None:
            return []
        
        location = list(location)[0]
        return location.split(', ')

    def define_estado(self):
        location_list = self.convert_location_on_list()
        
        if location_list == []:
            return None

        elif 'Ciudad de México' in location_list:
            return 'Ciudad de México'
        elif 'Estado de México' in location_list:
            return 'Estado de México'
        else:
            raise ValueError("Estado no reconocido", location_list)

    def define_alcaldia(self):
        estado = self.define_estado()
        if estado == None:
            return None

        location_list = self.convert_location_on_list()
        try:
            index_referencia = location_list.index(estado)
        except Exception as e:
            print(e, location_list, self.covert_to_point)
            return None

        index_referencia = index_referencia - 1
        alcaldia = location_list[index_referencia]

        return alcaldia



class Metrobus(Geolocalizacion):
    metrobus_id = models.PositiveSmallIntegerField(unique=True)
    alcaldia = models.ForeignKey(Alcaldia, on_delete=models.SET_NULL, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_altitud = self.altitud
        self.__original_longitud = self.longitud

    def __str__(self):
        return 'Metrobus ' + str(self.metrobus_id)

    def update_alcaldia(self):
        estado = self.define_estado()

        if estado == None:
            return None

        estado, estado_created = Estado.objects.get_or_create(nombre=estado)
        alcaldia = self.define_alcaldia()
        if alcaldia == None:
            return None

        alcaldia, alcaldia_created = Alcaldia.objects.get_or_create(nombre=alcaldia, estado=estado)
        self.alcaldia = alcaldia
        self.save()

    def save(self, *args, **kwargs):
        if self.__original_altitud != self.altitud or self.__original_longitud != self.longitud:
            self.update_alcaldia()
            
        super(Metrobus, self).save(*args, **kwargs)