from rest_framework import serializers
from ..models import InfoEvento


class EventoInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoEvento
        fields = ('description_tag', 'first_name', 'last_name', 'foto', 'permanencia',)