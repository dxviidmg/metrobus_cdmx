from .models import State, TownHall
from rest_framework import serializers

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class TownHallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TownHall
        fields = '__all__'


class TownHallMetrobusSerializer(serializers.HyperlinkedModelSerializer):
    metrobuses = serializers.HyperlinkedRelatedField(many=True,  read_only=True, view_name='metrobus-detail',)

    class Meta:
        model = TownHall
        fields = '__all__'