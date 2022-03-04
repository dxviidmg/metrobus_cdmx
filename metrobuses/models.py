from django.db import models
from alcaldias.models import State, TownHall
from geopy.geocoders import Nominatim


class Geolocation(models.Model):
    """
    Clase abstracta para la geolocalización de un punto
    """
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        abstract = True

    def convert_to_str(self):
        """Return point in text string"""
        return str(self.latitude) + ', ' + str(self.longitude)

    def get_location(self):
        """Get location through geopy"""
        geographic_point = self.convert_to_str()
        geolocator = Nominatim(user_agent="http")
        try:
            location = geolocator.reverse(geographic_point, timeout=10)
        except Exception as e:
            location = None
            print('error', e)
#            input()
        
        return location

    def convert_location_to_list(self):
        """ Convert location to list, this make easy the processing of location data"""
        location = self.get_location()
        if location == None:
            return []
        
        location = list(location)[0]
        return location.split(', ')

    def define_state(self):
        location_list = self.convert_location_to_list()
        
        if location_list == []:
            return None

        elif 'Ciudad de México' in location_list:
            return 'Ciudad de México'
        elif 'Estado de México' in location_list:
            return 'Estado de México'
        else:
            raise ValueError("Estado no reconocido", location_list)

    def define_townhall(self):
        state = self.define_state()
        if state == None:
            return None

        location_list = self.convert_location_to_list()
        try:
            reference_index = location_list.index(state)
        except Exception as e:
            print(e, location_list, self.covert_to_point)
            return None

        reference_index = reference_index - 1
        townhall = location_list[reference_index]

        return townhall



class Metrobus(Geolocation):
    number = models.PositiveSmallIntegerField(unique=True)
    townhall = models.ForeignKey(TownHall, on_delete=models.SET_NULL, null=True, blank=True, related_name='metrobuses')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_latitude = self.latitude
        self.__original_longitude = self.longitude

    def __str__(self):
        return 'Metrobus ' + str(self.number)

    def update_townhall(self):
#        print('start update_townhall')
        state = self.define_state()

        if state == None:
            return None

        state, state_created = State.objects.get_or_create(name=state)
        townhall = self.define_townhall()
        if townhall == None:
            return None

        townhall, townhall_created = TownHall.objects.get_or_create(name=townhall, state=state)
#        print(townhall)
        self.townhall = townhall
#        print('end update_townhall')
#        self.save()

    def save(self, *args, **kwargs):
        if self.__original_latitude != self.latitude or self.__original_longitude != self.longitude:
            self.update_townhall()
            
        super(Metrobus, self).save(*args, **kwargs)