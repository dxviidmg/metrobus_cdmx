from metrobuses.serializers import MetrobusSerializer
from .models import Alcaldia
from rest_framework import serializers


class AlcaldiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcaldia
        fields = '__all__'


class AlcaldiaMetrobusSerializer(serializers.ModelSerializer):
    metrobuses = serializers.StringRelatedField(many=True)


    class Meta:
        model = Alcaldia
        fields = '__all__'