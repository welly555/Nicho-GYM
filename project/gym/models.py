from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class Academia(AbstractUser):
    Nome_academia = models.CharField(max_length=254)
    cnpj = models.CharField(max_length=18)
    Endereco = models.CharField(max_length=254)
    telefone = models.CharField(max_length=15)
    password = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=255, null=True, unique=True)

    def __str__(self):
        return self.Nome_academia


class Aluno(models.Model):
    Nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    E_mail = models.EmailField(max_length=254)
    Data_Nascimento = models.DateField()
    Data_pagamento = models.DateField(
        null=True, default=timezone.now() + timedelta(days=30))
    Valor_pagamento = models.CharField(max_length=10)
    Situacao = models.BooleanField()
    Data_inscricao = models.DateField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    academia = models.ForeignKey(
        Academia, on_delete=models.CASCADE, null=True, blank=True, default=None)  # noqa: E501

    def __str__(self):
        return self.Nome


class Personal(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=100)
    E_mail = models.EmailField(max_length=254)
    telefone = models.IntegerField(default=None)
    academia = models.ForeignKey(
        Academia, on_delete=models.CASCADE, null=True, blank=True, default=None)  # noqa: E501

    def __str__(self):
        return self.Nome


class Risco(models.Model):
    Problema = models.CharField(max_length=300)
    Recomendacao = models.CharField(max_length=300)
    academia = models.ForeignKey(
        Academia, on_delete=models.CASCADE, null=True, blank=True, default=None)  # noqa: E501
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.Problema


class TipoAvaliacao(models.Model):
    tipo = models.CharField(max_length=150)

    def __str__(self):
        return self.tipo


class Avaliacao(models.Model):
    academia = models.ForeignKey(
        Academia, on_delete=models.CASCADE, null=True, blank=True, default=None)  # noqa: E501
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, null=True, blank=True, default=None)
    TipoAvaliacao = models.ForeignKey(
        TipoAvaliacao, on_delete=models.CASCADE, null=True, blank=True, default=None)  # noqa: E501
    Data_avaliacao = models.TimeField(auto_now_add=True)
    peso = models.FloatField()
    altura = models.FloatField()
    Dobra_tripical = models.FloatField()
    Dobra_abdominal = models.FloatField()
    Dobra_subescapular = models.FloatField()
    Dobra_axilar_media = models.FloatField(null=True)
    Dobra_coxa = models.FloatField(null=True)
    Dobra_toracica = models.FloatField(null=True)
    Dobra_suprailiaca = models.FloatField()
    Circoferencia_pescoco = models.FloatField(null=True)
    Circoferencia_torax = models.FloatField(null=True)
    Circoferencia_ombro = models.FloatField(null=True)
    Circoferencia_cintura = models.FloatField(null=True)
    Circoferencia_quadril = models.FloatField(null=True)
    Circoferencia_abdomen = models.FloatField(null=True)
    Circoferencia_braco_relaxado = models.FloatField(null=True)
    Circoferencia_braco_contraido = models.FloatField(null=True)
    Circoferencia_antebraco = models.FloatField(null=True)
    Circoferencia_prox_coxa = models.FloatField(null=True)
    Circoferencia_medial_coxa = models.FloatField(null=True)
    Circoferencia_distal_coxa = models.FloatField(null=True)
    Circoferencia_panturilha_coxa = models.FloatField(null=True)

    # def __str__(self):
    #     return self.Data_avaliacao
