from django.test import TestCase
from alcaldias.models import State, TownHall

class StateTestCase(TestCase):
    def setUp(self):
        State.objects.create(name='Ciudad de México')

    def test_create(self):
        state = State.objects.get(name='Ciudad de México')
        self.assertEqual(state.name, 'Ciudad de México')

class TownHallTestCase(TestCase):
    def setUp(self):
        state = State.objects.create(name='Ciudad de México')
        TownHall.objects.create(name='Álvaro Obregón', state=state)

    def test_create(self):
        townhall = TownHall.objects.get(name='Álvaro Obregón')
        self.assertEqual(townhall.name, 'Álvaro Obregón')