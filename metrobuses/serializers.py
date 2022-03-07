from .models import Metrobus
from rest_framework import serializers


class MetrobusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metrobus
        fields = '__all__'