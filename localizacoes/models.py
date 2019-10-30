from django.db import models

class Localizacao(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)



