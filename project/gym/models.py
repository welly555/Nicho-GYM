from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.


class Academia(models.Model):
    Nome_academia = models.CharField(max_length=254)
    Dono = models.CharField(max_length=254)
    E_mail = models.EmailField(max_length=254)
    cnpj = models.CharField(max_length=18)
    Endereco = models.CharField(max_length=254)
    senha = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.Nome_academia


class Aluno(models.Model):
    Nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    E_mail = models.EmailField(max_length=254)
    Data_Nascimento = models.DateField()
    Data_pagamento = models.DateField(auto_now_add=True)
    Valor_pagamento = models.FloatField()
    Situacao = models.BooleanField(default=True)
    Data_inscricao = models.DateField(auto_now_add=True)
    telefone = models.IntegerField(default=None)
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
        TipoAvaliacao, on_delete=models.SET_NULL, null=True, blank=True, default=None)  # noqa: E501
    Data_avaliacao = models.TimeField(auto_now_add=True)
    peso = models.FloatField()
    altura = models.FloatField()
    altura = models.FloatField()
    Dobra_tripical = models.FloatField()
    Dobra_abdominal = models.FloatField()
    Dobra_subescapular = models.FloatField()
    Dobra_axilar_media = models.FloatField()
    Dobra_coxa = models.FloatField()
    Dobra_toracica = models.FloatField()
    Dobra_suprailiaca = models.FloatField()
    Circoferencia_pescoco = models.FloatField()
    Circoferencia_torax = models.FloatField()
    Circoferencia_ombro = models.FloatField()
    Circoferencia_cintura = models.FloatField()
    Circoferencia_quadril = models.FloatField()
    Circoferencia_abdomen = models.FloatField()
    Circoferencia_braco_relaxado = models.FloatField()
    Circoferencia_braco_contraido = models.FloatField()
    Circoferencia_antebraco = models.FloatField()
    Circoferencia_prox_coxa = models.FloatField()
    Circoferencia_medial_coxa = models.FloatField()
    Circoferencia_distal_coxa = models.FloatField()
    Circoferencia_panturilha_coxa = models.FloatField()

    def __str__(self):
        return self.Data_avaliacao
