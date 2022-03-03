from .models import Metrobus
from rest_framework import serializers


class MetrobusSerializer(serializers.ModelSerializer):
#    owner = serializers.HiddenField(
#        default=serializers.CurrentUserDefault()
#    )
    class Meta:
        model = Metrobus
        fields = '__all__'