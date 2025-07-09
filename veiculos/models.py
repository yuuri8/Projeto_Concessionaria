from django.db import models

class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quilometragem = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
