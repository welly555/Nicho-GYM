# Generated by Django 4.2 on 2023-05-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_alter_academia_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
