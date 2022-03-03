from metrobuses.serializers import MetrobusSerializer
from .models import Alcaldia, Estado
from rest_framework import serializers

class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class AlcaldiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alcaldia
        fields = '__all__'


class AlcaldiaMetrobusSerializer(serializers.HyperlinkedModelSerializer):
    metrobuses = serializers.HyperlinkedRelatedField(many=True,  read_only=True, view_name='metrobus-detail',)

    class Meta:
        model = Alcaldia
        fields = '__all__'