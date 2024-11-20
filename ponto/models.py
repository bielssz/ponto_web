from django.db import models
from django.utils.timezone import now


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    entrada = models.DateTimeField(null=True, blank=True)
    checkout = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.entrada} - {self.checkout if self.checkout else 'Em aberto'}"