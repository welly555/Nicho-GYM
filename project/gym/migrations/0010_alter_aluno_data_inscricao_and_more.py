# Generated by Django 4.2 on 2023-05-28 19:32

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_alter_aluno_valor_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='Data_inscricao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='Data_pagamento',
            field=models.DateField(default=datetime.datetime(2023, 6, 27, 19, 32, 9, 588751, tzinfo=datetime.timezone.utc)),
        ),
    ]