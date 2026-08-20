from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        Administrador = "Administrador", "Administrador"
        Usuario = "Usuario", "Usuario" 
    
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.Usuario
    )
    
    def __str__(self):
        return self.get_full_name() or self.username

class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    logradouro = models.CharField(max_length=200)
    cep = models.CharField(max_length=12)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    
    def __str__(self):
        return self.titulo
    
class Contrato(models.Model):
    data_inicio =models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    locador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING,related_name="locador")
    locatario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name="locatario")
    
    def __str__(self):
        return f"Contrato {self.id}"
    
class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name="contrato")        

    def __str__(self):
        return f"Pagamento nº {self.id}"    