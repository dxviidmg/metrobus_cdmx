from django.test import TestCase
from alcaldias.models import State, TownHall
from metrobuses.models import Metrobus

class MetrobusTestCase(TestCase):
    def setUp(self):
        state = State.objects.create(name='Ciudad de México')
        TownHall.objects.create(name='Coyoacán', state=state)
        metrobus = Metrobus.objects.create(number=1)

    def test_create(self):
        metrobus = Metrobus.objects.get(number=1)
        self.assertEqual(metrobus.number, 1)

    def test_update(self):
        metrobus = Metrobus.objects.get(number=1)
        metrobus.latitude = 19.3174991607666
        metrobus.longitude = -99.1877975463867
        metrobus.save()

        self.assertEqual(metrobus.townhall.name, 'Coyoacán')