from django.contrib import admin

from .models import Academia, Aluno, Avaliacao, Personal, Risco, TipoAvaliacao

# Register your models here.

admin.site.register(
    [Academia, Aluno, Personal, Risco, Avaliacao, TipoAvaliacao])
