from django.db import models
from atracoes.models import Atracao
from localizacoes.models import Localizacao
from comentarios.models import Comentario
from reviews.models import Review

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=155)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    localizacao = models.OneToOneField(Localizacao, on_delete=models.SET_NULL, null=True)
    comentarios = models.ManyToManyField(Comentario)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.nome
