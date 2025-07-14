from django.contrib.auth.models import User
from django.db import models

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    permissao = models.CharField(max_length=20, choices=[('admin', 'Administrador'), ('vendedor', 'Vendedor')])

    def __str__(self):
        return self.nome
