from metrobuses.models import Metrobus
from rest_framework import viewsets
from metrobuses.serializers import MetrobusSerializer


class MetrobusViewSet(viewsets.ModelViewSet):
    queryset = Metrobus.objects.all()
    serializer_class = MetrobusSerializer