from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    
    nome = models.CharField(max_length=100)
    permissao = models.CharField(max_length=20, choices=[('admin', 'Administrador'), ('vendedor', 'Vendedor')])

    def __str__(self):
        return self.nome