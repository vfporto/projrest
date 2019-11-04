from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.usuario.username + " " + self.nota.to_eng_string()

