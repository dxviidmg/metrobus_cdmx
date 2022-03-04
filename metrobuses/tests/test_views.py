from django.test import TestCase
from metrobuses.models import Metrobus
from rest_framework.test import APIClient
from rest_framework import status


class TownHallTestCase(TestCase):
    def setUp(self):
        Metrobus.objects.create(number=1)

    def test_get_list(self):
        client = APIClient()
        response = client.get(
                '/metrobuses/metrobus/', {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_one(self):
        client = APIClient()
        response = client.get(
                '/metrobuses/metrobus/1/', {},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)