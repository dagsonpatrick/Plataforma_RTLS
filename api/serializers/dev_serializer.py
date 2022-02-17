from rest_framework import serializers
from ..models import Dev,EventoDevAWS

class DevSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventoDevAWS
        fields = '__all__'