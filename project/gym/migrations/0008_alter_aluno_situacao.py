# Generated by Django 4.2 on 2023-05-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_alter_aluno_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='Situacao',
            field=models.BooleanField(),
        ),
    ]
