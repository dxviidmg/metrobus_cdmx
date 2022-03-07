from alcaldias.models import State, TownHall 
from rest_framework import viewsets
from alcaldias.serializers import TownHallSerializer, TownHallMetrobusSerializer, StateSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class TownHallViewSet(viewsets.ModelViewSet):
    queryset = TownHall.objects.all().order_by('state', 'name')
    serializer_class = TownHallSerializer


    def retrieve(self, request, pk=None):
        town_hall = get_object_or_404(TownHall, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = TownHallMetrobusSerializer(town_hall, context=serializer_context)
        return Response(serializer.data)