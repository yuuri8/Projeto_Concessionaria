from django.db import models
from clientes.models import Cliente
from funcionarios.models import Funcionario
from veiculos.models import Veiculo

class Venda(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    data = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda de {self.veiculo} para {self.cliente}"

# Create your models here.
