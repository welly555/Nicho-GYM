# Generated by Django 4.2 on 2023-04-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_alter_academia_cnpj_alter_academia_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academia',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
