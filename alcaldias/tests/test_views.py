from django.test import TestCase
from alcaldias.models import State, TownHall
from rest_framework.test import APIClient
from rest_framework import status


class StateTestCase(TestCase):
    def setUp(self):
        State.objects.create(name='Ciudad de México')

    def test_get_list(self):
        client = APIClient()
        response = client.get(
                '/alcaldias/estado/', {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_one(self):
        client = APIClient()
        response = client.get(
                '/alcaldias/estado/1/', {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TownHallTestCase(TestCase):
    def setUp(self):
        state = State.objects.create(name='Ciudad de México')
        TownHall.objects.create(name='Álvaro Obregón', state=state)

    def test_get_list(self):
        client = APIClient()
        response = client.get(
                '/alcaldias/alcaldia/', {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_one(self):
        client = APIClient()
        response = client.get(
                '/alcaldias/alcaldia/1/', {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)