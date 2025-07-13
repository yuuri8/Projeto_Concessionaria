from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from veiculos.models import Veiculo
from funcionarios.models import Funcionario

class TestDrive(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('confirmado', 'Confirmado'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')])