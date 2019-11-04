from rest_framework.viewsets import ModelViewSet

from localizacoes.models import Localizacao
from .serializers import LocalizacaoSerializer
from rest_framework import viewsets


class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
