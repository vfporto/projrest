from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'localizacao__linha1']

    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True)
    #
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    #
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

