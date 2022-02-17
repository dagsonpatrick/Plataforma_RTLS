from rest_framework import serializers
from ..models import InfoPlanta


class PlantaInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoPlanta
        fields = ('id_plano', 'name_plano', 'description_plano', 'foto_plano', 'qtd_colaborador',)
