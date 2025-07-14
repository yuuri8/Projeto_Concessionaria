from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome