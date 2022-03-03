from alcaldias.models import Alcaldia 
from rest_framework import viewsets
from alcaldias.serializers import AlcaldiaSerializer, AlcaldiaMetrobusSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class AlcaldiaViewSet(viewsets.ModelViewSet):
    queryset = Alcaldia.objects.all().order_by('estado', 'nombre')
    serializer_class = AlcaldiaSerializer


    def retrieve(self, request, pk=None):
        queryset = Alcaldia.objects.all()
        alcaldia = get_object_or_404(queryset, pk=pk)
        serializer = AlcaldiaMetrobusSerializer(alcaldia)
        return Response(serializer.data)