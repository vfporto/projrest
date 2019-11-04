from rest_framework import serializers

from localizacoes.models import Localizacao


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['linha1', 'linha2', 'cidade', 'estado', 'pais']
