from alcaldias.models import Estado, Alcaldia 
from rest_framework import viewsets
from alcaldias.serializers import AlcaldiaSerializer, AlcaldiaMetrobusSerializer, EstadoSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class AlcaldiaViewSet(viewsets.ModelViewSet):
    queryset = Alcaldia.objects.all().order_by('estado', 'nombre')
    serializer_class = AlcaldiaSerializer


    def retrieve(self, request, pk=None):
        alcaldia = get_object_or_404(Alcaldia, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = AlcaldiaMetrobusSerializer(alcaldia, context=serializer_context)
        return Response(serializer.data)